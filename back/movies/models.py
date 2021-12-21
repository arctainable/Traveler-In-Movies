from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Genre(models.Model):
    tmdb_genre_id = models.IntegerField()
    name = models.CharField(max_length=50)


class Movie(models.Model):
    # 장르와 N:M 관계
    genres = models.ManyToManyField(Genre, related_name='movies')

    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    popularity = models.FloatField()
    vote_count = models.BigIntegerField()
    vote_avg   = models.FloatField()
    user_vote_count = models.BigIntegerField(default=0)
    user_vote_avg = models.FloatField(default=0)
    country_name = models.CharField(max_length=100)
    # aditional data
    director_path = models.CharField(max_length=500)
    director_name = models.CharField(max_length=100)
    actor1_path = models.CharField(max_length=500)
    actor1_name = models.CharField(max_length=100)
    actor2_path = models.CharField(max_length=500)
    actor2_name = models.CharField(max_length=100)
    actor3_path = models.CharField(max_length=500)
    actor3_name = models.CharField(max_length=100)
    actor4_path = models.CharField(max_length=500)
    actor4_name = models.CharField(max_length=100)        
    actor5_path = models.CharField(max_length=500)
    actor5_name = models.CharField(max_length=100)
    backdrop_path = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Director(models.Model):
    id = models.BigIntegerField(primary_key=True)
    movies = models.ManyToManyField(Movie, related_name='directors')
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Actor(models.Model):
    id = models.BigIntegerField(primary_key=True)
    movies = models.ManyToManyField(Movie, related_name='actors')
    name = models.CharField(max_length=100)
    profile_path = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movies')

    like_users = models.ManyToManyField(User, related_name='like_reviews')

    title = models.CharField(max_length=100)
    rank = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # foreignKey로 넘겨줄 때 부모 클래스에 _set 으로 해당 값을 넘겨준다 review_set 이런 식으로 Review 클래스에 값이 추가된다.
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content


class VoteRate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='movie_rate')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='user_rate')
    rate = models.FloatField()


class Preference(models.Model):
    matching = models.TextField(max_length=100)
    similar = models.IntegerField()


