from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.db import connection
from property import views as property_views
from property.models import Property, Review
from userprofile import views as userprofile_views
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
        property_views.addProperty(request)
        
        # Add a review
        property_id = Property.objects.get(title = 'Mansion').id
        request = self.factory.post('/property/' + str(property_id),
                                    {'review' : 'Property was as advertised',
                                    'starrating' : 5})
        request.user = self.user
        property_views.property(request, property_id)
        
        # Check to see if the profile view is able to retrieve the new review
        c = Client()
        response = c.get('/profile/' + str(self.user.id) + '/')
        review = response.context['reviews']
        self.assertNotEqual(review, None)
        if (review):
            self.assertEqual(review[0].text, 'Property was as advertised')
            self.assertEqual(review[0].rating, 5)
        
    def tearDown(self):
        Property.objects.all().delete()
        Review.objects.all().delete()