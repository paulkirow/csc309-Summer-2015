from django.shortcuts import render

from property.models import Review


def profile(request, userid):

    context = {}

    reviews = Review.objects.filter(property__user__id=userid)
    valid_ratings = [review.rating for review in reviews if review.rating]
    avg_rating = float(sum(valid_ratings)) / len(valid_ratings)
    context["avg_rating"] = avg_rating
    print(avg_rating)

    return render(request, "profile.html", context)
