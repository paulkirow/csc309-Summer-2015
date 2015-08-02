from django.shortcuts import render

from property.models import Property, Review


def profile(request, userid):

    context = {}

    properties = Property.objects.filter(user__id=userid)
    context["properties"] = properties

    reviews = Review.objects.filter(user__id=userid)
    context["reviews"] = reviews

    reviews = Review.objects.filter(property__user__id=userid)
    valid_ratings = [review.rating for review in reviews if review.rating]
    avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    context["avg_rating"] = avg_rating

    return render(request, "profile.html", context)
