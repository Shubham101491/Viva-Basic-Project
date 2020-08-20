from django.shortcuts import render
from viva import settings

def index(request):
    return render(request,'home/index.html',{"BASE_URL":settings.Base_url})