from django.shortcuts import render
from viva import settings

def sms(request):
    return render(request,'sms/sms.html',{"BASE_URL":settings.Base_url})
