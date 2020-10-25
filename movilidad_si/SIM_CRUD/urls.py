from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('citizen/license/create', views.createLicence, name='createLicence')
]
