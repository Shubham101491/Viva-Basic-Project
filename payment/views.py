from django.shortcuts import render
from viva import settings

def payment(request):
    return render(request,'payment/payment.html',{"BASE_URL":settings.Base_url})