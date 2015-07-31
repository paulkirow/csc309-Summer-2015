from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    user = models.ForeignKey(User)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    size = models.IntegerField(default=0)
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

class Tag(models.Model):
    property = models.ForeignKey(Property)
    tag = models.CharField(max_length=100)

class Rating(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User)
    text = models.IntegerField(default=0)

class Review(models.Model):
    property = models.ForeignKey(Property)
    user = models.ForeignKey(User)
    rating = models.ForeignKey(Rating)
    text = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)
