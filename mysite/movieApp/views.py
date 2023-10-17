from django.shortcuts import render, HttpResponse
from .models import Movie
# Create your views here.
def home(request):
    return render(request, "home.html")

def moviesPage(request):
    return render(request, "moviesPage.html", {"movies": Movie.objects.all()})


