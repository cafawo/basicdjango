# https://docs.djangoproject.com/en/2.2/topics/forms/
# https://docs.djangoproject.com/en/2.2/ref/forms/fields/

from django import forms

class SomeForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=200, required=False)
    last_name = forms.CharField(label='Last name', max_length=200, required=True)
    first_number = forms.FloatField(label='First number', required=True, initial=0)
    second_number = forms.FloatField(label='Second number', required=True, initial=0)
    reset_form = forms.BooleanField(label='Reset form', required=False, initial=False)