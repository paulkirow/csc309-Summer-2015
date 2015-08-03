from django.shortcuts import render

from property.models import Property, Review
from django.contrib.auth.models import User


def profile(request, userid):

    context = {}

    user = User.objects.get(pk=userid)
    context["username"] = user

    properties = Property.objects.filter(user__id=userid).order_by("-date_added")
    context["properties"] = properties

    reviews = Review.objects.filter(user__id=userid)
    context["reviews"] = reviews

    reviews = Review.objects.filter(property__user__id=userid).order_by("-date_added")
    valid_ratings = [review.rating for review in reviews if review.rating]
    avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    context["avg_rating"] = avg_rating

    return render(request, "profile.html", context)
