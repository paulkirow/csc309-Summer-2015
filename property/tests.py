from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from property import views
from property.models import Property
import re

# views test
class TestAddProperty(TestCase):
    
    def setUp(self):
        # Set up a test factory (so that request objects can be created later on)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='admin', email='admin@asdfasdf.com', password='123456')     
        
    def test_add_property(self):
        # Create a mock POST request
        request = self.factory.post('/addProperty/', 
                                    {'title' : 'Mansion', 
                                     'address' : '1000 Military Drive', 
                                     'city' : 'Toronto', 
                                     'province' : 'Ontario',
                                     'size' : '10000.0',
                                     'text' : 'Test',
                                     'user' : 'admin'})
        request.user = self.user
        views.addProperty(request)
        
        # Check to see if all of the fields for the property were added
        property = Property.objects.get(title="Mansion")
        self.assertEqual(property.address, '1000 Military Drive')
        self.assertEqual(property.city, 'Toronto')
        self.assertEqual(property.province, 'Ontario')
        self.assertEqual(property.size, 10000)
        self.assertEqual(property.text, 'Test')
        
    def test_add_property_not_logged_in(self):
        # Try to access the add property page without logging in
        c = Client()
        response = c.get('/addProperty/')
        result = re.match(r'^.*\/accounts\/login\/\?next=\/addProperty.*$', response.url)
        # Check to see if the url that the client was redirected to was in fact
        # the url for the login page
        self.assertNotEqual(result, None)
        
    def test_add_property_redirect(self):
        # See if successfully adding a property will redirect the user
        # to the home page
        c = Client()
        response = c.post('/addProperty/', 
                            {'title' : 'Mansion', 
                            'address' : '1000 Military Drive', 
                            'city' : 'Toronto', 
                            'province' : 'Ontario',
                            'size' : '10000.0',
                            'text' : 'Test',
                            'user' : 'admin'})
        result = re.match(r'^http:\/\/[a-z]*\/$', response.url)
        # Check to see if the user was redirected to the main page after
        # submitting a new property
        self.assertEqual(result, None)
        
class TestHomePage(TestCase):
    
    def setUp(self):
        # Set up a test factory (so that request objects can be created later on)
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='admin', email='admin@asdfasdf.com', password='123456') 
        
    def test_home_page_with_multiple_properties(self):
        # Add a single property to the database
        Property.objects.create(title='Mansion',
                                address = '1000',
                                city = 'Toronto',
                                province = 'Ontario',
                                size = '10000',
                                text = 'Test',
                                user = self.user)
        Property.objects.create(title='Mansion 2',
                                address = '1100',
                                city = 'Toronto',
                                province = 'Ontario',
                                size = '10000',
                                text = 'Test',
                                user = self.user)
        c = Client()
        # Check to see if those two properties were added to the property 
        # listing page
        response = c.get('/')
        # The view should show two properties
        self.assertEqual(len(response.context['properties']), 2)
        # There should only be 1 page overall
        self.assertEqual(response.context['current_page'], 1)
        self.assertEqual(response.context['total_page_number'], 1)
    
    def tearDown(self):
        Property.objects.all().delete()