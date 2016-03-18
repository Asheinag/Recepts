from django.conf.urls import include, url
from django.contrib import admin
from main.api import ReceptResource


recept_resource = ReceptResource()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls', namespace='main')),
    url(r'^api/', include(recept_resource.urls)),
]
