from django.shortcuts import render
from viva import settings
from django.contrib import messages
from datetime import datetime
from contact.models import Contact

def contact(request):
    return render(request,'contact/contact.html',{"BASE_URL": settings.Base_url})

def msg(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request, 'contact/contact.html',{"BASE_URL": settings.Base_url,'msg':'We will Contact you as soon....'})