from django.forms import ModelForm
from django import forms


class SearchUserForm(forms.Form):
    fields_name = forms.ChoiceField()
    fields_value = forms.CharField()

    class Meta:
        fields = ['fields_name', 'fields_value']
