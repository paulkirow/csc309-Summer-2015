from django.shortcuts import render

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
    return render(request, "addProperty.html", {})

def register(request):
    return render(request, "register.html", {})
