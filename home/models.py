from django.db import models

# Create your models here.

class Contact(models.Model):
    def __init__(self, Name,email,phone,desc):
        self.Name=models.CharField(max_length=122)
        self.email=models.CharField(max_length=122)
        self.phone=models.CharField(max_length=122)
        self.desc=models.CharField(max_length=122)
    # Name=models.CharField(max_length=122)
    #email=models.CharField(max_length=122)
    #phone=models.CharField(max_length=122)
    #desc=models.TextField()
    #date=models.DateField() 
