from rest_framework import serializers
from .models import Movie, Review, Comment, Genre, Director, Actor, VoteRate

from accounts.serializers import UserProfileSerializer
from django_summernote.widgets import SummernoteWidget


class CommentSerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id', 'user_id', 'review_id', 'content', 'created_at', 'updated_at', 'user',)
        read_only_fields = ('review_id',)


class ReviewSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    comments_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user = UserProfileSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user_id', 'movie_id', 'title', 
        'rank', 'content', 'created_at', 'updated_at'
        , 'comments', 'comments_count', 'user')
        read_only_fields = ('movie_id', 'user')


# 영화 리스트 Read용
class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'genres',
            'title',
            'overview',
            'poster_path',
            'popularity',
            'poster_path', 
            'vote_count', 
            'vote_avg', 
            'user_vote_count', 
            'user_vote_avg',
            'country_name',
            'director_path',
            'director_name',
            'actor1_path',
            'actor1_name',
            'actor2_path',
            'actor2_name',
            'actor3_path',
            'actor3_name',
            'actor4_path',
            'actor4_name',
            'actor5_path',
            'actor5_name',            
            'backdrop_path',
        )

# 단일 영화 Read용
class MovieSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    reviews_count = serializers.IntegerField(source='reviews.count', read_only=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'genres',
            'title',
            'overview',
            'poster_path',
            'popularity',
            'poster_path', 
            'vote_count', 
            'vote_avg', 
            'user_vote_count', 
            'user_vote_avg',
            'country_name',
            'reviews',
            'reviews_count',
        )

class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'

class ActorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class VoteRateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = VoteRate
        fields = ('id', 'user', 'movie', 'rate',)
        read_only_fields = ('user', 'movie',)







