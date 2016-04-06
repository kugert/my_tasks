from django.forms import ModelForm
from django import forms
from .models import *


class AddCocktailNameForm(ModelForm):
    class Meta:
        model = Cocktail
        fields = ['cocktail_name']


class AddComponentsForm(ModelForm):
    class Meta:
        model = Compose
        fields = ['ingredients', 'ingredient_value', 'measures']


class IngredientCount(forms.Form):
    ingredient_count = forms.IntegerField(max_value=10, min_value=1)
