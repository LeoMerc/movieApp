from django.shortcuts import render, HttpResponse
from .models import Movie, Genre, Studio, Person, Role, MovieReview, MovieCredit
# Create your views here.
def home(request):
    return render(request, "home.html")

def moviesPage(request):
    # items =[ Movie.objects.all(), Genre.objects.all(), Studio.objects.all(), Person.objects.all(), Role.objects.all(), MovieCredit.objects.all(), MovieReview.objects.all() ]
    return render(request, "moviesPage.html", {"movies": Movie.objects.all(),
                                               "genres": Genre.objects.all(),
                                               "studios": Studio.objects.all(),
                                               "people": Person.objects.all(),
                                               "roles": Role.objects.all(),
                                               "movieCredits": MovieCredit.objects.all(),
                                               "movieReviews": MovieReview.objects.all()}
                  
                  )


