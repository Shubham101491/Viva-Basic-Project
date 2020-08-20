from django.db import models

class Userdata(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=300)
    Zipcode = models.IntegerField(max_length=10)
    password = models.CharField(max_length=20)