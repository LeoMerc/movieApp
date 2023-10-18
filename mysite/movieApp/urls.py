from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('recommendedMovies/', views.recommendedMovies, name='recommendedMovies'),
 ]