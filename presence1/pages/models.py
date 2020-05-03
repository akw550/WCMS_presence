from django.db import models

# Create your models here.

class ContactModel(models.Model):
    name = models.CharField(max_length=50, null=True)
    # rollno = models.BigIntegerField(null= True)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=20)


    objects = models.Manager

