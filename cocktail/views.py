from django.shortcuts import render, get_object_or_404, redirect
from .models import Cocktail
from .forms import *
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory


def index(request):
    cocktail_list = Cocktail.objects.all()
    context = {'cocktail_list': cocktail_list}
    return render(request, 'cocktail/index.html', context)


def detail(request, cocktail_id):
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    cocktail_list = Cocktail.objects.all()
    return render(request, 'cocktail/detail.html', {'cocktail': cocktail,
                                                    'cocktail_list': cocktail_list})


def add_cocktail(request):
    cocktail_form = AddCocktailNameForm()
    add_ingredients = IngredientCount()
    components_form = formset_factory(AddComponentsForm, extra=0)
    if 'add_ingredient' in request.POST:
        count = request.POST['ingredient_count']
        components_form = formset_factory(AddComponentsForm, extra=int(count))
    if 'create' in request.POST:
        new_cocktail_form = AddCocktailNameForm(request.POST)
        new_cocktail = new_cocktail_form.save(commit=False)
        cocktail_id = new_cocktail.pk
        new_cocktail.save()
        '''not working
        ------------------------------------------------'''
        new_components = components_form(request.POST)
        for component in new_components.cleaned_data:
            component.save(commit=False)
            query = Compose(cocktails=cocktail_id,
                            ingredients=component.ingredients,
                            ingredient_value=component.ingredient_value,
                            measures=component.measures)
            query.save()

        '''
        ------------------------------------------------'''
        return redirect('detail', cocktail_id)
    '''if request.method == 'POST':
        new_cocktail_form = AddCocktailNameForm(request.POST)
        new_cocktail_form.save()
        return redirect('../')'''
    return render(request, 'cocktail/add.html', {'cocktail_name_form': cocktail_form,
                                                 'add_ingredients': add_ingredients,
                                                 'components_form': components_form})
