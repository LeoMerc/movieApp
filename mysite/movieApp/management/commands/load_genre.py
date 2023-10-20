import os
import requests
from  datetime import datetime, date, timezone 
import sys
from django.core.management.base import BaseCommand, CommandError
import requests

import json 
from movieApp.models import Genre, Movie, Person, Role, Studio, MovieCredit
from dotenv import load_dotenv
import os

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_dotenv()
        
    
        url = "https://api.themoviedb.org/3/genre/movie/list?language=en"

        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('ApiKey')}"
        }

        response = requests.get(url, headers=headers)

        data = response.json()
        
        for g in data["genres"]:
            new_genre = Genre.objects.get_or_create(name=g["name"], tmdb_id=g["id"])


        url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

        headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('ApiKey')}"
        }

        response = requests.get(url, headers=headers)

        data = response.json()
        
        for d in data['results']:
            url = f"https://api.themoviedb.org/3/movie/{d['id']}?append_to_response=credits&language=en-US"

            headers = {
                "accept": "application/json",
                "Authorization": f"Bearer {os.getenv('ApiKey')}"
            }

            response = requests.get(url, headers=headers)

            data = response.json()

            studio_id = Studio.objects.get_or_create(name=data["production_companies"][0]["name"])

            new_movie = Movie.objects.get_or_create(title=data["original_title"],
            country=data["production_countries"][0]["name"], 
            release_date=data["release_date"], 
            description=data["overview"], 
            duration=data["runtime"], 
            budget=data["budget"], 
            gross=data["revenue"], 
            classification=data["adult"], 
            tmdb_id=data["id"], 
            studiofK=studio_id[0],
            img_path=data["poster_path"], )

            for g in data["genres"]:
                genre_id = Genre.objects.get(tmdb_id=g["id"])
                new_movie[0].genresfK.add(genre_id)
            
          

            for c in data["credits"]["cast"][:10]:
            
                url = f"https://api.themoviedb.org/3/person/{c['id']}?language=en-US"

                

                headers = {
                    "accept": "application/json",
                    "Authorization": f"Bearer {os.getenv('ApiKey')}"
                }

                print(headers)
                response = requests.get(url, headers=headers)

                data = response.json()

                new_person = Person.objects.get_or_create(name=data["name"], 
                birthday=data["birthday"], 
                country=data["place_of_birth"],
                img_path=data["profile_path"])

                new_role = Role.objects.get_or_create(name="Actor")

                new_movie_credit = MovieCredit.objects.get_or_create(person=new_person[0], movie=new_movie[0], role=new_role[0])
                new_movie[0].credits.add(new_movie_credit[0].person)
                


