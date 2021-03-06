# Generated by Django 3.2.8 on 2021-11-24 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_genre_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('poster_path', models.CharField(max_length=500)),
                ('popularity', models.FloatField()),
                ('vote_count', models.BigIntegerField()),
                ('vote_avg', models.FloatField()),
                ('user_vote_count', models.BigIntegerField(default=0)),
                ('user_vote_avg', models.FloatField(default=0)),
                ('country_name', models.CharField(max_length=100)),
                ('director_path', models.CharField(max_length=500)),
                ('director_name', models.CharField(max_length=100)),
                ('actor1_path', models.CharField(max_length=500)),
                ('actor1_name', models.CharField(max_length=100)),
                ('actor2_path', models.CharField(max_length=500)),
                ('actor2_name', models.CharField(max_length=100)),
                ('actor3_path', models.CharField(max_length=500)),
                ('actor3_name', models.CharField(max_length=100)),
                ('actor4_path', models.CharField(max_length=500)),
                ('actor4_name', models.CharField(max_length=100)),
                ('actor5_path', models.CharField(max_length=500)),
                ('actor5_name', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(max_length=500)),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matching', models.TextField(max_length=100)),
                ('similar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='VoteRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.FloatField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_rate', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_rate', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('rank', models.IntegerField()),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('like_users', models.ManyToManyField(related_name='like_reviews', to=settings.AUTH_USER_MODEL)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movies', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(max_length=500)),
                ('movies', models.ManyToManyField(related_name='directors', to='movies.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(max_length=500)),
                ('movies', models.ManyToManyField(related_name='actors', to='movies.Movie')),
            ],
        ),
    ]
