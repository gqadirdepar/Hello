from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    name = models.CharField(max_length=50)
    age =  models.CharField(max_length=50)


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    age =  models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=50)
    age =  models.CharField(max_length=50)