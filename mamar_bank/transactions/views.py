from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.http import HttpResponse
from django.views.generic import CreateView, ListView
from accounts.models import UserBankAccount
from core.models import Bankrupt
from .contants import DEPOSIT, WITHDRAWAL, LOAN, LOAN_PAID, TRANSFER
from datetime import datetime
from django.db.models import Sum
from transactions.forms import (
    DepositForm,
    WithdrawForm,
    LoanRequestForm, BalanceTransferForm,
)
from transactions.models import Transaction
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string

def send_transaction_email(user, amount,  mail_subject, template_name):
    message_body = render_to_string(template_name, {
        'user': user,
        'amount': amount,
        'timestamp': timezone.now(),
    })

    email = EmailMultiAlternatives(
        mail_subject,
        '',
        '',
        [user.email],
    )
    email.attach_alternative(message_body, "text/html")
    email.send()
    return email

class TransactionCreateMixin(LoginRequiredMixin, CreateView):
    template_name = 'transaction_form.html'
    model = Transaction
    title = ''
    success_url = reverse_lazy('transaction_report')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({
            'account': self.request.user.account
        })
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': self.title
        })

        return context


class DepositMoneyView(TransactionCreateMixin):
    form_class = DepositForm
    title = 'Deposit'

    def get_initial(self):
        initial = {'transaction_type': DEPOSIT}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance += amount
        account.save(
            update_fields=[
                'balance'
            ]
        )

        send_transaction_email(self.request.user, amount, 'Deposit Money', 'deposit_email.html')

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)


class WithdrawMoneyView(TransactionCreateMixin):
    form_class = WithdrawForm
    title = 'Withdraw Money'

    def get_initial(self):
        initial = {'transaction_type': WITHDRAWAL}
        return initial

    def form_valid(self, form):
        bankrupt_status = Bankrupt.objects.first().is_bankrupt

        if bankrupt_status:
            messages.error(
                self.request,
                f'Bank is bankrupt, you can not withdraw money'
            )
            return redirect('transaction_report')

        amount = form.cleaned_data.get('amount')
        self.request.user.account.balance -= form.cleaned_data.get('amount')
        self.request.user.account.save(update_fields=['balance'])

        send_transaction_email(self.request.user, amount, 'Withdraw Money', 'withdraw_email.html')

        messages.success(
            self.request,
            f'Successfully withdrawn {"{:,.2f}".format(float(amount))}$ from your account'
        )

        return super().form_valid(form)

class LoanRequestView(TransactionCreateMixin):
    form_class = LoanRequestForm
    title = 'Request For Loan'

    def get_initial(self):
        initial = {'transaction_type': LOAN}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        current_loan_count = Transaction.objects.filter(
            account=self.request.user.account,transaction_type=3,loan_approve=True).count()
        if current_loan_count >= 3:
            return HttpResponse("You have cross the loan limits")


        send_transaction_email(self.request.user, amount, 'Loan Request', 'loan_email.html')

        messages.success(
            self.request,
            f'Loan request for {"{:,.2f}".format(float(amount))}$ submitted successfully'
        )

        return super().form_valid(form)

class TransactionReportView(LoginRequiredMixin, ListView):
    template_name = 'transaction_report.html'
    model = Transaction
    balance = 0

    def get_queryset(self):
        queryset = super().get_queryset().filter(
            account=self.request.user.account
        )
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')

        if start_date_str and end_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()

            queryset = queryset.filter(timestamp__date__gte=start_date, timestamp__date__lte=end_date)
            self.balance = Transaction.objects.filter(
                timestamp__date__gte=start_date, timestamp__date__lte=end_date
            ).aggregate(Sum('amount'))['amount__sum']
        else:
            self.balance = self.request.user.account.balance

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'account': self.request.user.account
        })

        return context


class PayLoanView(LoginRequiredMixin, View):
    def get(self, request, loan_id):
        loan = get_object_or_404(Transaction, id=loan_id)
        if loan.loan_approve:
            user_account = loan.account
            if loan.amount < user_account.balance:
                user_account.balance -= loan.amount
                loan.balance_after_transaction = user_account.balance
                user_account.save()
                loan.loan_approved = True
                loan.transaction_type = LOAN_PAID
                loan.save()
                return redirect('loan_list')
            else:
                messages.error(
                    self.request,
                    f'Loan amount is greater than available balance'
                )

        return redirect('loan_list')


class LoanListView(LoginRequiredMixin,ListView):
    model = Transaction
    template_name = 'loan_request.html'
    context_object_name = 'loans'

    def get_queryset(self):
        user_account = self.request.user.account
        queryset = Transaction.objects.filter(account=user_account,transaction_type=3)
        return queryset


class BalanceTransferView(TransactionCreateMixin):
    template_name = 'balance_transfer.html'
    form_class = BalanceTransferForm
    model = Transaction
    title = 'Balance Transfer'
    success_url = reverse_lazy('transaction_report')

    def get_initial(self):
        initial = {'transaction_type': TRANSFER}
        return initial

    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')
        receiver_account_number = form.cleaned_data.get('receiver_account_number')

        sender_account = self.request.user.account
        try:
            receiver_account = UserBankAccount.objects.get(account_no=receiver_account_number)
        except UserBankAccount.DoesNotExist:
            form.add_error('receiver_account_number', f'Account with account number {receiver_account_number} not found')
            return self.form_invalid(form)

        if sender_account == receiver_account:
            form.add_error('receiver_account_number', 'You can not transfer money to your own account')
            return self.form_invalid(form)

        if sender_account.balance < amount:
            form.add_error('amount', 'Insufficient balance in your account')
            return self.form_invalid(form)


        self.request.user.account.balance -= amount
        receiver_account.balance += amount
        self.request.user.account.save(update_fields=['balance'])
        receiver_account.save(update_fields=['balance'])

        Transaction.objects.create(
            account=receiver_account,
            amount=amount,
            transaction_type=TRANSFER,
            balance_after_transaction=receiver_account.balance,
        )

        sender_message_body = render_to_string('transaction_sender_email.html', {
            'sender_first_name': sender_account.user.first_name,
            'sender_last_name': sender_account.user.last_name,
            'receiver_first_name': receiver_account.user.first_name,
            'receiver_last_name': receiver_account.user.last_name,
            'amount': amount,
            'timestamp': timezone.now()
        })

        sender_email = EmailMultiAlternatives(
            'Transaction Sent Confirmation',
            '',
            '',
            [sender_account.user.email]
        )
        sender_email.attach_alternative(sender_message_body, "text/html")
        sender_email.send()

        receiver_message_body = render_to_string('transaction_receiver_email.html', {
            'sender_first_name': sender_account.user.first_name,
            'sender_last_name': sender_account.user.last_name,
            'receiver_first_name': receiver_account.user.first_name,
            'receiver_last_name': receiver_account.user.last_name,
            'amount': amount,
            'timestamp': timezone.now()
        })
        receiver_email = EmailMultiAlternatives(
            'Transaction Received Confirmation',
            '',
            '',
            [receiver_account.user.email]
        )
        receiver_email.attach_alternative(receiver_message_body, "text/html")
        receiver_email.send()

        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was transferred to account {receiver_account_number} successfully'
        )

        return super().form_valid(form)



