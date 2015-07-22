from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.db import connection

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
    """ Authentication doesn't work atm
    else:
        return HttpResponseRedirect('/')"""
    
    if request.method == 'GET':
        """context = {'user': user}"""
        return render(request, "addProperty.html", {})
    else:
        title = request.POST.get("title", "")
        address = request.POST.get("address", "")
        city = request.POST.get("city", "")
        province = request.POST.get("province", "")
        size = request.POST.get("size", "")
        text = request.POST.get("text", "")
        user = request.POST.get("user", "")
        
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM auth_user WHERE username = %s", [user])
        user_id = cursor.fetchone()
        cursor.execute("INSERT INTO property_property (title, address, city, province, size, text, user_id, date_added) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", 
                       [title, address, city, province, size, text, '9000', ''])
        return HttpResponseRedirect('/')

def register(request):
    return render(request, "register.html", {})
