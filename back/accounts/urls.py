from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('api-token-auth/', obtain_jwt_token),
    # 유저가 작성한 리뷰 조회 url
    path('profile/<int:user_pk>/reviews/', views.reviews, name='user_reviews'), 
    # 유저가 작성한 리뷰의 장르 목록 조회 url
    path('profile/<int:user_pk>/reviews/genre/', views.reviews_genre, name='user_reviews_genre'),
    # 유저가 작성한 리뷰의 나라목록 조회 url
    path('profile/<int:user_pk>/reviews/country/', views.reviews_country, name='user_reviews_country'),
    # 유저가 작성한 리뷰의 영화 데이터 조회 url
    path('profile/<int:user_pk>/reviews/movies/', views.reviews_movies, name='user_reviews_movies'),

    # 유저가 작성한 리뷰 영화의 장르별, 나라별 영화 목록을 조회 url,
    path('profile/<int:user_pk>/reviews/genre_country_movies/', views.genre_country_movies, name='user_genre_movies'),

]