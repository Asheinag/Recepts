from tastypie.resources import ModelResource
from .models import Recept


class ReceptResource(ModelResource):
    class Meta:
        queryset = Recept.objects.all()
        resource_name = 'recept'
