from django.db import models

class Employee(models.Model):
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    experience = models.IntegerField()
    designation = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    class Meta:
        db_table = "employee"
    def __str__(self):
        return self.name
