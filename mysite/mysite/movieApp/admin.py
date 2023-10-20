from django.contrib import admin
from .models import Movie, Genre, Studio, Person, Role, MovieReview, MovieCredit
# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Studio)
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(MovieReview)
admin.site.register(MovieCredit)