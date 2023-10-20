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
def movie(request):
    return render(request, "movie.html", {"movieind": Movie.objects,
                                               "genres": Genre.objects,
                                               "studios": Studio.objects,
                                               "people": Person.objects,
                                               "roles": Role.objects,
                                               "movieCredits": MovieCredit.objects,
                                               "movieReviews": MovieReview.objects}
                  
                  )

def cast(request):
    return render(request, "cast.html", {"cast": Movie.objects,
                                               "genres": Genre.objects,
                                               "studios": Studio.objects,
                                               "people": Person.objects,
                                               "roles": Role.objects,
                                               "movieCredits": MovieCredit.objects,
                                               "movieReviews": MovieReview.objects}
                  
                  )


