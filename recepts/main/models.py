# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Recept(models.Model):
    name = models.CharField('Рецепт', max_length=200)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField('Ингредиент', max_length=200)

    def __str__(self):
        return self.name


class VariationIng(models.Model):
    ing = models.ForeignKey(Ingredient)
    new_name = models.CharField(max_length=200)


class InList(models.Model):
    recept = models.ForeignKey(Recept)
    ving = models.ForeignKey(VariationIng, default=None)
