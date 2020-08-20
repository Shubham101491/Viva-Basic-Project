from django.urls import path
from . import views

urlpatterns = [
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('login/enter/',views.enter,name='enter'),
    path('logout/',views.logout,name='logout'), 
]