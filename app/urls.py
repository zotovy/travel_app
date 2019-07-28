from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flights', views.home_flights, name='home_flights'),
    path('hotel', views.home_hotel, name='home_hotel'),
    path('contact', views.contact, name='contact'),
    path('dev', views.dev, name='dev')
]