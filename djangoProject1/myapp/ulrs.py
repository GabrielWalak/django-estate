from django.urls import path
from .views import lista_nieruchomosci
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('nieruchomosci/', lista_nieruchomosci, name='lista_nieruchomosci'),
]