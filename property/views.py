from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.db import connection
from django.contrib.auth.decorators import login_required
import os.path
import datetime

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

from .models import Property, Review

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
        username = "%s" % (request.user)
    context = {
            "username":username,
    }

    property = Property.objects.get(pk=property_id)
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

def search(request):
    return render(request, "search.html", {})

@login_required
def addProperty(request):
    user = request.user

    if request.method == 'GET':
        context = {'user': user}
        return render(request, "addProperty.html", context)
    else:
        title = request.POST.get("title", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        province = request.POST.get("province", "")
        size = request.POST.get("size", "")
        text = request.POST.get("text", "")
        user = request.POST.get("user", "")
        if (len(request.FILES) > 0):
            fType = request.FILES['my-file-selector'].name.split('.', 2)[1]
            # Files will be named like usernamejan02.jpg
            if (fType != ""):
                fType = '.' + fType
            handle_uploaded_file(request.FILES['my-file-selector'],
                                 user +
                                 str(datetime.datetime.now()).translate(None, " :") +
                                 fType)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM auth_user WHERE username = %s", [user])
        user_id = cursor.fetchone()[0]
        cursor.execute("INSERT INTO property_property (title, address, city, province, size, text, user_id, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       [title, address, city, province, size, text, user_id, datetime.datetime.now()])
        return HttpResponseRedirect('/')

def handle_uploaded_file(f, name):
    destination = open(os.path.join(os.path.dirname(os.path.dirname(__file__)),'pub\\img\\' + name), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()

def register(request):
    return render(request, "register.html", {})
