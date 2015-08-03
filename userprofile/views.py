from django.shortcuts import render

from property.models import Property, Review
from django.core.paginator import Paginator

def profile(request, userid):

    context = {}

    properties = Property.objects.filter(user__id=userid)
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


    reviews = Review.objects.filter(property__user__id=userid)
    valid_ratings = [review.rating for review in reviews if review.rating]
    avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    context["avg_rating"] = avg_rating
    context["posts"] = posts
    return render(request, "profile.html", context)
