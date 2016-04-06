from django.db import models


class Measure(models.Model):
    measure_name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.measure_name


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.ingredient_name


class Cocktail(models.Model):
    cocktail_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.cocktail_name


class Compose(models.Model):
    cocktails = models.ForeignKey(Cocktail)
    ingredients = models.ForeignKey(Ingredient)
    measures = models.ForeignKey(Measure)
    ingredient_value = models.PositiveIntegerField()

    def __unicode__(self):
        return str(self.ingredient_value)
