from django.forms import ModelForm
from django import forms


class SearchUserForm(forms.Form):
    field_name = forms.ChoiceField()
    field_value = forms.CharField()

    class Meta:
        fields = ['fields_name', 'fields_value']
