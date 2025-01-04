from django import forms
from .models import Exhibition

class ExhibitionForm(forms.ModelForm):
    class Meta:
        model = Exhibition
        fields = ['title', 'description', 'start_date', 'end_date', 'section']
        widgets ={
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
