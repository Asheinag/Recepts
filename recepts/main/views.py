# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Recept, Ingredient, InList, VariationIng

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'main/index.html'
    context_object_name = 'recepts'

    def get_queryset(self):
        return Recept.objects.order_by('name')


class ReceptView(generic.DetailView):
    model = Recept
    template_name = 'main/recept.html'

