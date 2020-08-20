from django.shortcuts import render, HttpResponse, redirect
from viva import settings
from signup.models import Userdata

def signup(request):
    return render(request,'signup/signup.html',{'BASE_URL': settings.Base_url})

def login(request):
    user    = request.POST.get("name")
    mail    = request.POST.get("email")
    contact = request.POST.get("contact")
    address = request.POST.get("address")
    zipcode = request.POST.get("zipcode")
    pwd     = request.POST.get("password")
    data = Userdata(username=user, email=mail, contact=contact, address=address, Zipcode=zipcode, password=pwd)
    data.save()
    return render(request,'signup/login.html',{'BASE_URL': settings.Base_url})   

def enter(request):
    user = request.POST.get("name")
    pwd  = request.POST.get("password")
    all_objects = Userdata.objects.filter(username=user, password=pwd)
    if(all_objects):
        return render(request,'signup/wel.html', {'data': all_objects})
    else:
        return HttpResponse("<h1>user id or pwd is wrong</h1>")

def logout(request):
    return render (request,'Thankyou for shopping Here')