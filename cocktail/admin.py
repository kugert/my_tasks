from django.contrib import admin
from .models import *

admin.site.register(Ingredient)
admin.site.register(Measure)


class ComposeInline(admin.TabularInline):
    model = Compose
    extra = 1
    fields = ['ingredients', 'ingredient_value', 'measures']


class CocktailAdmin(admin.ModelAdmin):
    fields = ['cocktail_name']
    inlines = [ComposeInline]


admin.site.register(Cocktail, CocktailAdmin)
