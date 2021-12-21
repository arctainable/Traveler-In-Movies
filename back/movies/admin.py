from django.contrib import admin
from .models import Movie, Review, Comment, Genre, Director, Actor, VoteRate

class MovieAdmin(admin.ModelAdmin):
    moviefields = ['title', 'overview', 'poster_path', 'popularity', 'vote_count', 'vote_avg', 'user_vote_count', 'user_vote_avg', 'country_name']

class ReviewAdmin(admin.ModelAdmin):
    reviewfields = ['user', 'movie', 'title', 'movie_title',  'rank', 'content', 'created_at', 'updated_at']

class CommentAdmin(admin.ModelAdmin):
    commentfields = ['user','review','content', 'created_at','updated_at']

class GenreAdmin(admin.ModelAdmin):
    genrefields = ['tmdb_genre_id', 'name']

class DirectorAdmin(admin.ModelAdmin):
    directorfields = ['name','profile_path']

class ActorAdmin(admin.ModelAdmin):
    actorfields = ['name','profile_path']

class VoteRateAdmin(admin.ModelAdmin):
    voteratefields = ['user','movie','rate']

admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Director, DirectorAdmin)
admin.site.register(Actor, ActorAdmin)
admin.site.register(VoteRate, VoteRateAdmin)