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


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'), 
    path('create_trajet/', create_trajet_api, name='create_trajet'),
    path('trajets/<int:pk>/', TrajetDetailView.as_view(), name='trajet-detail'),
     path('trajetss/<int:pk>/', delete_trajet, name='trajet-detail'),
    path('trajetslien/', trajet_list, name='trajetslien'),
]


