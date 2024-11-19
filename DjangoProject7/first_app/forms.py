from django import forms

from first_app.models import StudentModel


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__'
        # fields = ('name', 'roll')
        # exclude = ('father_name', 'address')
        labels = {
            'name': 'Student Name',
            'roll': 'Roll Number',
            'father_name': 'Father Name',
            'address': 'Address',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'roll': forms.NumberInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
        }
        help_texts = {
            'name': 'Enter your name',
            'roll': 'Enter your roll number',
            'father_name': 'Enter your father name',
            'address': 'Enter your address',
        }
        error_messages = {
            'name': {
                'required': 'Name is required',
                'max_length': 'Name should not exceed 20 characters',
            },
            'roll': {
                'required': 'Roll number is required',
                'invalid': 'Enter a valid roll number',
            },
            'father_name': {
                'required': 'Father name is required',
                'max_length': 'Father name should not exceed 20 characters',
            },
            'address': {
                'required': 'Address is required',
            },
        }
