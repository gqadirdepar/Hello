from django.db import models

# Create your models here.

class Contact(models.Model):
    Name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    #date=models.DateField() 
