from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.db import connection
import os.path
import datetime

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

# Create your views here.
def home(request):
    username = "Register"
    if (request.user.is_authenticated()):
        username = "%s" % (request.user)
    context = {
            "username":username,
    }

    return render(request, "home.html", context)

def search(request):
    return render(request, "search.html", {})

def addProperty(request):
    if (request.user.is_authenticated()):
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
        print len(request.FILES)
        print datetime.date.today()
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
