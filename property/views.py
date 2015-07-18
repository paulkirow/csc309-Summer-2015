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

def register(request):
    return render(request, "register.html", {})