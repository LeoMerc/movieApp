from django.shortcuts import render, HttpResponse, redirect
from .models import Movie, Genre, Studio, Person, Role, MovieReview, MovieCredit
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django import views
from .forms import UserRegisterForm
from django.shortcuts import render, HttpResponse
from .models import (
    Movie,
    Genre,
    Studio,
    Person,
    Role,
    MovieReview,
    MovieCredit,
    MiFormulario,
)
from .forms import MovieReviewForm


# Create your views here.


     
class Register(views.View):
        def get(self, request):
            form = UserRegisterForm()
            return render(request, "register.html", {"form": form})

        def post(self, request):
            # render form with POST body data
            form = UserRegisterForm(request.POST)

            # check if form is vaild
            if form.is_valid():
                new_user = form.save()

                # if valid, save form and authenticate user
                new_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'])

                login(request, new_user)

            # redirect when finished
            return redirect('home')

def home(request):
    return render(
        request,
        "home.html",
        {
            "movies": Movie.objects.all(),
            "genres": Genre.objects.all(),
            "studios": Studio.objects.all(),
            "people": Person.objects.all(),
            "roles": Role.objects.all(),
            "movieCredits": MovieCredit.objects.all(),
            "movieReviews": MovieReview.objects.all(),
        },
    )


def recommendedMovies(request):
    return render(
        request,
        "recommendedMoviesPage.html",
        {
            "movies": Movie.objects.all(),
            "genres": Genre.objects.all(),
            "studios": Studio.objects.all(),
            "people": Person.objects.all(),
            "roles": Role.objects.all(),
            "movieCredits": MovieCredit.objects.all(),
            "movieReviews": MovieReview.objects.all(),
        },
    )


def movie(request):
    return render(
        request,
        "movie.html",
        {
            "movieind": Movie.objects,
            "genres": Genre.objects,
            "studios": Studio.objects,
            "people": Person.objects,
            "roles": Role.objects,
            "movieCredits": MovieCredit.objects,
            "movieReviews": MovieReview.objects,
        },
    )


def cast(request):
    return render(
        request,
        "cast.html",
        {
            "cast": Movie.objects,
            "genres": Genre.objects,
            "studios": Studio.objects,
            "people": Person.objects,
            "roles": Role.objects,
            "movieCredits": MovieCredit.objects,
            "movieReviews": MovieReview.objects,
        },
    )


# Función para traer la informaación basandonos en el id de la base de datos
def movieInformation(request, idDB):
    movie = Movie.objects.get(tmdb_id=idDB)
    print("----------")
    print(movie)
    print(movie.genresfK)
    print(movie.credits.all())
    # movieC = Movie.credits.get(tmdb_id=idDB)
    # movie.credits.through.objects.filter(movie=movie)
    return render(
        request,
        "movie.html",
        {"movie": movie},
    )


def castInformation(request, idDB):
    person = Person.objects.get(id=idDB)
    print(person)
    # pit = MovieCredit.objects.get(tmdb_id=idDB)
    movieCredits = MovieCredit.objects.filter()
    # print(movieCredits)
    # print(pit.all())
    print("CASTINFORMATION")
    # movieC = Movie.credits.get(tmdb_id=idDB)
    # movie.credits.through.objects.filter(movie=movie)
    return render(
        request,
        "cast.html",
        {"movie": movie, "person": person},
    )

# def login_user(request):
#     if request.method=="POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         print(username)
#         print(password)
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             print("User is not none")
#             login(request, user)
#             return redirect("");
#             ...
#         else:
#             messages.info(request, "Username or password is incorrect")
#             return redirect("login");



#     else:
#         return render(
#             request,
#             "login.html",
#             {},
#         )

def formReview(request):
    form = MovieReviewForm(request.POST)
    if form.is_valid():
        form.save()

    return render(request, "review.html", {"form": form})
