from django.db import models
from django.contrib.auth.models import User

# Create your models here.


"""class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    verified = models.BooleanField(default=False)
    type = models.IntegerField(defult=0)
    email = models.EmailField(max_length=254)
    username = models.CharField(max_length=20)
    password ="""

class Property(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

class Tags(models.Model):

class Rating(models.Model):

class Review(models.Model):
