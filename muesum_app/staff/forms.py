from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['first_name', 'last_name', 'position', 'hire_date']
        widgets ={
            'hire_date': forms.DateInput(attrs={'type': 'date'}),
        }