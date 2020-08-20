"""viva URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include

# these lines are import for Media
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')),
    path('blog/',include('blog.urls')),
    path('mail/',include('mail.urls')),
    path('sms/',include('sms.urls')),
    path('shop/',include('shop.urls')),
    path('signup/',include('signup.urls')),
    path('contact/',include('contact.urls')),
    path('payment/',include('payment.urls')),
    path('api/',include('api.urls')),
    path('emp', views.emp),
    path('show',views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.delete),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)