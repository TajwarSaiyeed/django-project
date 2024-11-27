from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import GeeksModel

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class InputFrom(forms.Form):
    name = forms.CharField(
        max_length = 10,
        initial='Your name'
    )
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(
        label="Please enter your email address",
        required = False,
    )
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}), initial=datetime.date.today)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)

    FAVORITE_COLORS_CHOICES = [
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    ]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_color_radio = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors_checkbox = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)


class GeeksModelForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = "__all__"
        exclude = ['time_field', 'uuid_field']
        labels = {
            "title": "Title",
            "description": "Description",
            "url_field": "URL Field",
        }
        help_texts = {
            "title": "Enter the title",
            "description": "Enter the description",
            "url_field": "Enter the URL",
        }
        error_messages = {
            "title": {
                "max_length": "This title is too long.",
            },
        }
        widgets = {
            "description": forms.Textarea(attrs={'rows': 3}),
        }
        field_classes = {
            "title": forms.CharField,
        }
        localized_fields = ['title']