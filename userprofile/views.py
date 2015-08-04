from django.shortcuts import render

from property.models import Property, Review
from django.core.paginator import Paginator
from django.contrib.auth.models import User


def profile(request, userid):

    context = {}

    user = User.objects.get(pk=userid)
    context["username"] = user

    properties = Property.objects.filter(user__id=userid).order_by("-date_added")
    context["properties"] = properties

    reviews = Review.objects.filter(user__id=userid)
    context["reviews"] = reviews

    paginator = Paginator(reviews, 5)

    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1

    try:
        posts = paginator.page(page)
    except(EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)


    reviews = Review.objects.filter(property__user__id=userid).order_by("-date_added")
    valid_ratings = [review.rating for review in reviews if review.rating]
    if len(valid_ratings) > 0:
        avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    else:
        avg_rating = 0
    context["avg_rating"] = avg_rating
    context["posts"] = posts
    return render(request, "profile.html", context)
