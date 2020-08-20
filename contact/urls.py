from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('msg/', views.msg, name='msg'),
]