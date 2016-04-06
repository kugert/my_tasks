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
        new_cocktail_form.save()
        added_cocktail = new_cocktail_form['cocktail_name'].value()
        last_added = Cocktail.objects.get(cocktail_name=added_cocktail)
        cocktail_id = last_added.id
        '''not working
        ------------------------------------------------'''
        new_components = components_form(request.POST)
        for component in new_components:
            '''query = Compose(cocktails=last_added,
                            ingredients=Ingredient.objects.get(id=component['ingredients'].value()),
                            ingredient_value=component['ingredient_value'].value(),
                            measures=Measure.objects.get(component['measures'].value())
                            )'''
            query = Compose.objects.create(cocktails=last_added,
                                           ingredients=Ingredient.objects.get(id=component['ingredients'].value()),
                                           ingredient_value=component['ingredient_value'].value(),
                                           measures=Measure.objects.get(component['measures'].value()))
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
