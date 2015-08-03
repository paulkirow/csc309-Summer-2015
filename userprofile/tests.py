from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.db import connection
from property import views
from property.models import Property
from userprofile import views
import re

# views test
class TestUserProfile(TestCase):
    
    def setUp(self):
        # Set up a test factory (so that request objects can be created later on)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='admin', email='admin@asdfasdf.com', password='123456')
        
    def test_add_rating(self):
        # Add a property
        request = self.factory.post('/addProperty/',
                                    {'title' : 'Mansion',
                                     'address' : '1000 Military Drive',
                                     'city' : 'Toronto',
                                     'province' : 'Ontario',
                                     'size' : 10000,
                                     'text' : 'Test',
                                     'user' : 'admin'})
        request.user = self.user
        views.addProperty(request)
        
        # Add a review
        
    def tearDown(self):
        Property.objects.all().delete()
        Review.objects.all.delete()