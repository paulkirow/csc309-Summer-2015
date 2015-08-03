from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
from django.db import connection
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from OpenYard import settings
from property.models import *
import os.path, datetime, math, re
from pydoc import describe
from django.core.serializers import json
import json
<<<<<<< HEAD
from django.core.paginator import Paginator
=======
from OpenYard import settings
>>>>>>> origin/master
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

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
    owner_email = User.objects.get(pk=property.user.id).email
    context["owner_email"] = owner_email

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

<<<<<<< HEAD
def search(request):

    
    return render(request, "search.html", {})   
   
=======
"""def search(request):

    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = Property(title=post_text)
        post.save()

        response_data['result'] = 'Create post successful!'
        response_data['text'] = post.text

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )"""
def search(request):
    query_string = ''
    found_entries = None
    if ('search' in request.GET) and request.GET['search'].strip():
        query_string = request.GET['search']

        entry_query = get_query(query_string, ['title', 'text', ])

        found_entries = Property.objects.filter(entry_query).order_by('-date_added')
    context = {"query_string": query_string, "found_entries": found_entries}
    return render(request, 'search.html', context)

def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in invidual keywords, getting rid of unecessary spaces
        and grouping quoted words together.
        Example:
        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']
        Reference: http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]

def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.
        Reference: http://julienphalip.com/post/2825034077/adding-search-to-a-django-site-in-a-snap
    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query

>>>>>>> origin/master
@login_required
def addProperty(request):
    user = request.user

    # A GET request from the user/client means that the user is trying
    # to access the form. So simply render the add property page in this case
    if request.method == 'GET':
        context = {'user' : user, 'notification' : ''}
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
            if (request.FILES['my-file-selector'].size > 10000000):
                # The file has to be < 10MB
                context = {'user' : user, 'notification' : 'The file can only be <10 MB!'}
                return render(request, "addProperty.html", context)
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
