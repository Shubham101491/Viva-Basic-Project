from django.urls import path
from . import views

urlpatterns = [
    # path('',views.mail,name='mail'),                 #  for 'send_mail'
    path('',views.mass_mail,name='mass_mail'),       # for  'send_mass_mail'
    # path('',views.admins,name='admins'),             # for 'mail_admins'
    # path('',views.managers,name='managers'),           # for 'mail_managers'
]