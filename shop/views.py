from django.shortcuts import render
from viva import settings

def shop(request):
    return render(request,'shop/shop.html',{"BASE_URL":settings.Base_url})
