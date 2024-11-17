from django import forms
from django.core import validators


# widgets = field to html input

class ContactForm(forms.Form):
    # my_photo = forms.ImageField(label='Your Image')
    # file= forms.FileField(label='Your File')
    # name = forms.CharField(label='Your Name', max_length=100, initial="Tajwar", required=False, disabled=True)
    name = forms.CharField(label='Your Name',
                           widget=forms.Textarea(attrs={'rows': 2, 'cols': 20, 'placeholder': 'Enter your name'}))
    email = forms.EmailField(label='Your Email', max_length=100)
    age = forms.IntegerField(label='Your Age')
    weight = forms.FloatField(label='Your Weight')
    balance = forms.DecimalField(label='Your Balance')
    check = forms.BooleanField(label='Check', required=False)
    # dob = forms.DateField(label='Your DOB')
    dob = forms.CharField(label='Your DOB',
                          widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'Enter your DOB'}))
    # appointment = forms.DateTimeField(label='Appointment')
    appointment = forms.CharField(label='Appointment', widget=forms.DateTimeInput(
        attrs={'type': 'datetime-local', 'placeholder': 'Enter your Appointment'}))
    CHOICES = [('S', 'Small'), ("M", "Medium"), ("L", "Large")]
    size = forms.ChoiceField(label='Size', choices=CHOICES, required=False)
    radioSize = forms.ChoiceField(label="Radio Size", choices=CHOICES,
                                  widget=forms.RadioSelect(attrs={'class': 'radio'}))
    MEAL = [('B', 'Breakfast'), ('L', 'Lunch'), ('D', 'Dinner')]
    pizza = forms.MultipleChoiceField(label='Pizza', choices=MEAL, widget=forms.CheckboxSelectMultiple)


class StudentData(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email', max_length=100)

    # def clean_name(self):
    #     valName = self.cleaned_data.get('name')
    #     if len(valName) < 5:
    #         raise forms.ValidationError("Name must be greater than 5 characters")
    #     return valName
    #
    # def clean_email(self):
    #     valEmail = self.cleaned_data.get('email')
    #     if '.com' not in valEmail:
    #         raise forms.ValidationError("Email must contain .com")
    #     return valEmail
    def clean(self):
        cleaned_data = super().clean()
        valName = cleaned_data.get('name')
        valEmail = cleaned_data.get('email')

        if not valName:
            raise forms.ValidationError("Name field is required.")
        if not valEmail:
            raise forms.ValidationError("Email field is required.")

        if len(valName) < 5:
            raise forms.ValidationError("Name must be greater than 5 characters")
        if '.com' not in valEmail:
            raise forms.ValidationError("Email must contain .com")


def len_check(value):
    if len(value) < 5:
        raise forms.ValidationError("Text must be greater than 5 characters")


class UserForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100, validators=[
        validators.MinLengthValidator(5, message="Name must be greater than 5 characters")])
    text = forms.CharField(label='Your address', max_length=100, validators=[len_check])
    email = forms.CharField(label='Your Email', widget=forms.EmailInput, max_length=100,
                            validators=[validators.EmailValidator(message='Enter a valid email')])
    age = forms.IntegerField(label='Your Age',
                             validators=[validators.MaxValueValidator(24), validators.MinValueValidator(18)])
    file = forms.FileField(label='Your File', validators=[
        validators.FileExtensionValidator(allowed_extensions=['pdf'], message='Only pdf files are allowed')])


class PasswordValidationProject(forms.Form):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        valPassword = cleaned_data.get('password')
        valConfirmPassword = cleaned_data.get('confirm_password')

        if valPassword != valConfirmPassword:
            raise forms.ValidationError("Password and Confirm Password must be same.")
