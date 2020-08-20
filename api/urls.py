from django.urls import path
from . import views

urlpatterns = [
    path('',views.PersonView.as_view(),name='Person'),
    path('add/', views.WeatherView.as_view(), name='Weather'),
]