from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('recommendedMovies/', views.recommendedMovies, name='recommendedMovies'),
    path('movie/', views.movie, name="movie"),
    path('cast/', views.cast,name="cast" )
 ]