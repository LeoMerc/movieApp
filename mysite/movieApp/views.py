from django.shortcuts import render, HttpResponse
from .models import Movie, Genre, Studio, Person, Role, MovieReview, MovieCredit
# Create your views here.
def home(request):
    return render(request, "home.html", {"movies": Movie.objects.all(),
                                               "genres": Genre.objects.all(),
                                               "studios": Studio.objects.all(),
                                               "people": Person.objects.all(),
                                               "roles": Role.objects.all(),
                                               "movieCredits": MovieCredit.objects.all(),
                                               "movieReviews": MovieReview.objects.all()}
                                               )

def recommendedMovies(request):
    return render(request, "recommendedMoviesPage.html", {"movies": Movie.objects.all(),
                                               "genres": Genre.objects.all(),
                                               "studios": Studio.objects.all(),
                                               "people": Person.objects.all(),
                                               "roles": Role.objects.all(),
                                               "movieCredits": MovieCredit.objects.all(),
                                               "movieReviews": MovieReview.objects.all()}
                  
                  )


