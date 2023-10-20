# Generated by Django 4.2.6 on 2023-10-17 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('country', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('description', models.TextField()),
                ('duration', models.IntegerField()),
                ('img_path', models.CharField(max_length=100)),
                ('gross', models.IntegerField()),
            ],
        ),
    ]
