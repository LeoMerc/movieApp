from django.http import Http404
from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from .models import Movie, Genre, Studio, Person, Role, MovieReview, MovieCredit
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
)
from .forms import MovieReviewForm
from django.db.models import Case, When


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
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password1"],
            )

            login(request, new_user)

        # redirect when finished
        return redirect("home")


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


    # Recommendation Algorithm based from rajaprerak's github https://github.com/rajaprerak
    # To get similar movies based on user rating
def get_similar(movie_name,rating,corrMatrix):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    return similar_ratings


def recommend(request):
  

    if not request.user.is_authenticated:
        return redirect("login")
    if not request.user.is_active:
        raise Http404


    movie_rating=pd.DataFrame(list(MovieReview.objects.all().values()))
   
    new_user=movie_rating.userfK_id.unique().shape[0]
   
    current_user_id= request.user.id
   
	# # if new user not rated any movie
    # if current_user_id>new_user:
    #     movie=Movie.objects.get(id=1)
    #     q=MovieReview(userfK=request.user,moviefK=movie,rating=0,review="")
    #     q.save()


    userRatings = movie_rating.pivot_table(index=['userfK_id'],columns=['moviefK_id'],values='rating')
    print("userRatings")
    print(userRatings)


    userRatings = userRatings.fillna(0,axis=1)
    corrMatrix = userRatings.corr(method='pearson')

    user = pd.DataFrame(list(MovieReview.objects.filter(userfK=request.user).values())).drop(['userfK_id','id','review'],axis=1)
    user_filtered = [tuple(x) for x in user.values]
    print("user_filtered")
    print(user_filtered)
    movie_id_watched = [each[0] for each in user_filtered]

    similar_movies = pd.DataFrame()
    for movie,rating in user_filtered:
        similar_movies = similar_movies._append(get_similar(movie,rating,corrMatrix),ignore_index = True)

    movies_id = list(similar_movies.sum().sort_values(ascending=False).index)
    movies_id_recommend = [each for each in movies_id if each not in movie_id_watched]
    preserved = Case(*[When(pk=pk, then=pos) for pos, pk in enumerate(movies_id_recommend)])
    movie_list=list(Movie.objects.filter(id__in = movies_id_recommend).order_by(preserved)[:10])

    context = {'movie_list': movie_list}
    print(movie_list)
    return render(request, 'recommendedMoviesPage.html', context)
   


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
    print(movie.tmdb_id)
    reviews = MovieReview.objects.filter(moviefK=movie)
    print("----------")
    studio = Studio.objects.filter(name=movie.studiofK)
    print(studio)
    # movieC = Movie.credits.get(tmdb_id=idDB)
    # movie.credits.through.objects.filter(movie=movie)
    return render(
        request,
        "movie.html",
        {"movie": movie, "reviews": reviews, "studio": studio},
    )


def castInformation(request, idDB):
    person = Person.objects.get(id=idDB)
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


# def getReviews(request, idDB):
#     movie = Movie.objects.get(tmdb_id=idDB)
#     reviews = MovieCredit.objects.filter(movie=movie)

#     print(reviews)
#     return render(request, "movie.html", {"review": reviews})


class formReview(views.View):
    def get(self, request, idDB, userID):
        movie = Movie.objects.get(tmdb_id=idDB)
        user = User.objects.get(id=userID)
        form = MovieReviewForm(initial={"moviefK": movie, "userfK": user})
        return render(request, "review.html", {"form": form})

    def post(self, request, idDB, userID):
            movie = Movie.objects.get(tmdb_id=idDB)
            user = User.objects.get(id=userID)
            print(movie)
            form = MovieReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.moviefK = movie
                review.userfK = user
                review.save()
                return redirect(request.META.get('HTTP_REFERER'))

            
            # # render form with POST body data
            # form = MovieReviewForm(request.POST)
            # # check if form is vaild
            # if form.is_valid():
            #     form.save()

               

    # # redirect when finished
    # return redirect('movieDetails')
