"""
URL configuration for bus_tracker_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from buses.views import RegisterView, LoginView
from buses.views import create_trajet_api
from buses.views import TrajetDetailView
from buses.views import trajet_list
from buses.views import delete_trajet

from buses.views import create_bus_api
from buses.views import BusDetailView
from buses.views import bus_list
from buses.views import delete_bus

from buses.views import create_conduct_api
from buses.views import ConductDetailView
from buses.views import conduct_list
from buses.views import delete_conduct

from buses.views import RelatBusTrajetListCreateView, RelatBusTrajetDetailView

from buses.views import  RelatBusTrajetSearchView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('create_trajet/', create_trajet_api, name='create_trajet'),
    path('trajets/<int:pk>/', TrajetDetailView.as_view(), name='trajet-detail'),
     path('trajetss/<int:pk>/', delete_trajet, name='trajet-detail'),
    path('trajetslien/', trajet_list, name='trajetslien'),

    path('create_bus/', create_bus_api, name='create_bus'),
    path('buss/<int:pk>/', BusDetailView.as_view(), name='bus-detail'),
     path('busss/<int:pk>/', delete_bus, name='bus-detail'),
    path('busslien/', bus_list, name='busslien'),

     path('create_conduct/', create_conduct_api, name='create_conduct'),
    path('conducts/<int:pk>/', ConductDetailView.as_view(), name='conduct-detail'),
     path('conductss/<int:pk>/', delete_conduct, name='conduct-detail'),
    path('conductslien/', conduct_list, name='conductslien'),

    path('relatbustrajet/', RelatBusTrajetListCreateView.as_view(), name='relatbustrajet-list-create'),
    path('relatbustrajet/<int:pk>/', RelatBusTrajetDetailView.as_view(), name='relatbustrajet-detail'),

    path('relat-bus-trajet/search/', RelatBusTrajetSearchView.as_view(), name='relat-bus-trajet-search'),

]
