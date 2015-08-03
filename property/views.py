from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.db import connection
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from property.models import *
from OpenYard import settings
import os.path
import datetime
from pydoc import describe

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

import math

def home(request):
    username = "Register"
    if (request.user.is_authenticated()):
        username = "%s" % (request.user)
    context = {
            "username":username,
    }

    #-- produce properties to display for the requested page
    #     display at most 16 properties each page

    # get requested page, default to the first page
    page_number = int(request.GET.get('p', 1))

    # get properties for the requested page
    start = (page_number - 1) * 16
    end   = page_number * 16 - 1
    properties = Property.objects.order_by("-date_added")[start:end + 1]
    context["properties"] = properties

    # page information
    context["current_page"] = page_number
    total_page_number = int(math.ceil(
        Property.objects.order_by("-date_added").count() / 16.0
    ))
    context["total_page_number"] = total_page_number

    return render(request, "home.html", context)

def property(request, property_id):
    username = "Register"
    if (request.user.is_authenticated()):
        username_cur = "%s" % (request.user)
        # A review is being added on a property
        if request.method == 'POST':
            review_new = request.POST.get("review", "")
            rating_new = request.POST.get("starrating", "")
            if rating_new == '': rating_new = 0
            user_cur = User.objects.filter(username=username_cur)[0]
            property_cur = Property.objects.filter(id=property_id)[0]
            Review(user=user_cur, property=property_cur, text=review_new, rating=rating_new).save()
            return HttpResponseRedirect('/property/%s' % property_id)
            
    context = {
                    "username":username,
            }
    property = Property.objects.get(id=property_id)
    context["property"] = property

    #-- produce reviews for the current property
    #     display at most 10 reviews at a time
    
    # get requested page, default to the first page
    page_number = int(request.GET.get('p', 1))

    # get reviews for the requested page
    start = (page_number - 1) * 10
    end   = page_number * 10 - 1
    reviews = Review.objects.filter(property=property_id).order_by("-date_added")[start:end + 1]
    context["reviews"] = reviews

    # page information
    context["current_page"] = page_number
    total_page_number = int(math.ceil(
        Property.objects.order_by("-date_added").count() / 10.0
    ))
    context["total_page_number"] = total_page_number
    return render(request, "property.html", context)

def searchproperty(request):
    
    if request.method == "POST":
        search_text = request.POST('search_text')
    else:
        search_text = ''
    
    property = Property.objects.filter(Q(title__contains=search_text) 
                                       | Q(text_contains=search_text)
                                       | Q(city__contains=search_text)
                                       | Q(province_contains=search_text)
                                       | Q(size__gte="1",size__let="100"))

    context["property"] = property
   
    
    return render(request, "search_results.html", context)

def search(request):
    
    context = {}
    context.update(csrf(request))
    context['property'] = Property.objects.all()
    
    return render(request, "search.html", context)

@login_required
def addProperty(request):
    user = request.user

    # A GET request from the user/client means that the user is trying
    # to access the form. So simply render the add property page in this case
    if request.method == 'GET':
        context = {'user': user}
        return render(request, "addProperty.html", context)
    else:
        # A POST request was probably submitted (which only happens when a user
        # submits a form, so get all of the information in the form 
        # submitted by the user
        title = request.POST.get("title", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        province = request.POST.get("province", "")
        size = request.POST.get("size", "")
        text = request.POST.get("text", "")
        user_name = request.POST.get("user", "")
        image_upload_time = datetime.datetime.now()
        image_name = ''
        if (len(request.FILES) > 0):
            fType = request.FILES['my-file-selector'].name.split('.', 2)[1]
            # Files will be named like username2015-08-01201015.312000.png
            if (fType != ""):
                fType = '.' + fType
            image_name = user_name + str(image_upload_time).translate(None, " :") + fType
            # Store the uploaded file in the server
            handle_uploaded_file(request.FILES['my-file-selector'],
                                 image_name)
        # Insert the records for the user's property into the database
        user = User.objects.get(username = user_name)
        property = Property(title = title,
                            address = address,
                            city = city,
                            province = province,
                            size = size,
                            text = text,
                            user = user,
                            image_name = image_name)
        property.save()
        return HttpResponseRedirect('/')

def handle_uploaded_file(f, name):
    # Divide the uploaded file into chunks, before uploading them onto the server
    destination = open(os.path.join(settings.USERIMG_DIR, name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def register(request):
    return render(request, "register.html", {})
