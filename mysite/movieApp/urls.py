from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("recommendedMovies/", views.recommend, name="recommendedMovies"),
    # path("movie/", views.movie, name="movie"),
    path("cast/<int:idDB>", views.castInformation, name="cast"),
    path("movies/<int:idDB>", views.movieInformation, name="movieDetails"),
    # path("login/", views.login_user, name="login"),
    path('register/', views.Register.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("form/<int:idDB>/<int:userID>/", views.formReview.as_view(), name="NewReview")
]
