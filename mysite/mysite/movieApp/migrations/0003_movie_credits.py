# Generated by Django 4.2.6 on 2023-10-17 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0002_genre_role_studio_remove_movie_year_movie_budget_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='credits',
            field=models.ManyToManyField(through='movieApp.MovieCredit', to='movieApp.person'),
        ),
    ]
