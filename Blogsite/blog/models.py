from django.db import models

class Profiles(models.Model):
    First_name = models.CharField(max_length=225)
    Username = models.CharField(max_length=32)
    email = models.CharField(max_length=50)
    Phone_number = models.IntegerField()    
