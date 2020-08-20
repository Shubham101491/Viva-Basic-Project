from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from api.serializers import DummySerializer

# this function is use for API
global data;
data = ['test']

class PersonView(APIView):
    # Create for Get Part
    def get(self, request, format=None):
        message = {
            'Response':200,
            'Message': "Welcome to Django Rest API",
            'data': data
        }
        return Response(message)

    # Create for Post Part
    def post(self, request, format=None):
        datam = request.data
        name = datam.get('name',None)
        data.append(name)
        message = {
            'Response':200,
            'Message': "Welcome to Django Rest API",
            'data': data
        }
        return Response(message)

# Create for Serializer.py file
class WeatherView(generics.CreateAPIView):
    serializer_class = DummySerializer
    def create(self, request, *args, **kwargs):
        try:
            zip = request.data.get('zip')
            city = request.data.get('city')
            age = request.data.get('age')
            return super().create(request, *args,**kwargs)
        except Exception as e:
            return Response({
                "Message": "Failed"
            })