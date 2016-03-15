from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
    # /
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /recept/1
    url(r'^(?P<pk>[0-9]+)/$', views.ReceptView.as_view(), name='recept'),
]
