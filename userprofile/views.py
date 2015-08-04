from django.shortcuts import render

from property.models import Property, Review


from django.core.paginator import Paginator


from django.core.paginator import Paginator

from django.contrib.auth.models import User
import os.path, datetime, math, re



def profile(request, userid):

    context = {}

    user = User.objects.get(pk=userid)
    context["username"] = user

    properties = Property.objects.filter(user__id=userid).order_by("-date_added")
    context["properties"] = properties

    reviews = Review.objects.filter(user__id=userid)
    context["reviews"] = reviews

    paginator = Paginator(reviews, 5)

    page_number = int(request.GET.get('p', 1))

    # get properties for the requested page
    start = (page_number - 1) * 10
    end   = page_number * 10 - 1
    reviews = Review.objects.filter(property__user__id=userid).order_by("-date_added")[start:end + 1]
    context["reviews"] = reviews


    # page information
    context["current_page"] = page_number
    total_page_number = int(math.ceil(
        Review.objects.filter(property__user__id=userid).order_by("-date_added").count() / 10.0
    ))
    context["total_page_number"] = total_page_number 
   

    reviews = Review.objects.filter(property__user__id=userid).order_by("-date_added")

    valid_ratings = [review.rating for review in reviews if review.rating]
    if len(valid_ratings) > 0:
        avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    else:
        avg_rating = 0
    context["avg_rating"] = avg_rating

    return render(request, "profile.html", context)
