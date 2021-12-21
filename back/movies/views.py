from django.db import reset_queries
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import response

from django.core import serializers
from .models import Movie, Preference, Review, Comment, Genre, Director, Actor, VoteRate
from .serializers import UserProfileSerializer, MovieListSerializer, MovieSerializer, ReviewSerializer, CommentSerializer, GenreSerializer, DirectorSerializer, ActorSerializer, VoteRateSerializer
from django.contrib.auth import get_user_model


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from django.core.paginator import Paginator
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


# recommend algorithm
import random
import collections


# 유저 모델 
User = get_user_model()

'''
메인 페이지
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all().order_by('?')
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page_num')
    movies = paginator.get_page(page_number)
    serializer = MovieListSerializer(movies, many=True)
    data = serializer.data
    data.append({'total_pages': paginator.num_pages})
    return Response(data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list_no(request):
    movies = Movie.objects.all().order_by('country_name')
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page_num')
    movies = paginator.get_page(page_number)
    serializer = MovieListSerializer(movies, many=True)
    data = serializer.data
    data.append({'total_pages': paginator.num_pages, 'total_count': paginator.count,})
    return Response(data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list_rate(request):
    movies = Movie.objects.all().order_by('-vote_avg')
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page_num')
    movies = paginator.get_page(page_number)
    serializer = MovieListSerializer(movies, many=True)
    data = serializer.data
    data.append({'total_pages': paginator.num_pages, 'total_count': paginator.count,})
    return Response(data)

@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list_popular(request):
    movies = Movie.objects.all().order_by('-popularity')
    paginator = Paginator(movies, 9)
    page_number = request.GET.get('page_num')
    movies = paginator.get_page(page_number)
    serializer = MovieListSerializer(movies, many=True)
    data = serializer.data
    data.append({'total_pages': paginator.num_pages, 'total_count': paginator.count,})
    return Response(data)

'''
메인 페이지(로그인 유저 선호도 기반)
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_recommend(request, username):
    # 유저 선호한 나라 3개 목록 저장
    personal = User.objects.get(username=username)
    personal_pref = personal.user_preference

    # 마지막 공백 제거하며 리스트 형태로 저장 (['LA', 'UK', 'SouthAfrica'])
    personal_pref = personal_pref.split('.')[0:3]

    # 첫번째로 고른 나라와 매칭되는 나라 중 가장 similar 값이 높은 순으로 2개 출력하여 저장
    first_pref = Preference.objects.filter(matching__startswith=personal_pref[0]).order_by('-similar').first()
    second_pref = Preference.objects.filter(matching__startswith=personal_pref[0]).order_by('-similar')[1]

    # 매칭된 나라 이름만 저장
    first = first_pref.matching.split('_')[1]
    second = second_pref.matching.split('_')[1]
    new_nation_list = [personal_pref[0], personal_pref[1], personal_pref[2], first, second]

    # 선호순위 1, 2, 3순위 / 유저들의 선호도를 반영한 순위 1, 2위 순으로 가중치를 두고 choice
    recommend = random.choices(new_nation_list, weights=[3, 2, 1, 1, 1], k=9)
    rec = collections.Counter(recommend)
    count1 = recommend.count(personal_pref[0])
    count2 = recommend.count(personal_pref[1])
    count3 = recommend.count(personal_pref[2])
    count4 = recommend.count(first)
    count5 = recommend.count(second)
    print(count1, count2, count3, count4, count5)
    convert = {
        'Brazil':'브라질',
        'Colombia':'콜롬비아',
        'Mexico':'멕시코',
        'LA':'라스베이거스',
        'Washington':'워싱턴',
        'Chicago':'시카고',
        'Canada':'캐나다',
        'Chile':'칠레',
        'Japan':'일본',
        'Hongkong':'홍콩',
        'China':'중국',
        'India':'인도',
        'Australia':'호주',
        'NewZleand':'뉴질랜드',
        'UK':'영국',
        'France':'프랑스',
        'Italy':'이탈리아',
        'SouthAfrica':'남아프리카공화국',
        'Somalia':'소말리아',
        'Moroco':'모로코',
    }

    reco_movie1 = Movie.objects.filter(country_name=convert[personal_pref[0]]).order_by('-vote_avg')[0:count1]
    if count2:
        reco_movie2 = Movie.objects.filter(country_name=convert[personal_pref[1]]).order_by('-vote_avg')[0:count2]
        movies = reco_movie1 | reco_movie2
    if count3:
        reco_movie3 = Movie.objects.filter(country_name=convert[personal_pref[2]]).order_by('-vote_avg')[0:count3]
        movies = movies | reco_movie3
    if count4:
        reco_movie4 = Movie.objects.filter(country_name=convert[first]).order_by('-vote_avg')[0:count4]
        movies = movies | reco_movie4
    if count5:
        reco_movie5 = Movie.objects.filter(country_name=convert[second]).order_by('-vote_avg')[0:count5]
        movies = movies | reco_movie5
    print(movies)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

'''
단일 영화 조회
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

'''
전체 리뷰 조회 및 생성
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def review_list(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    # 리뷰 조회
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_pk).order_by('-pk')
        paginator = Paginator(reviews, 5)
        page_number = request.GET.get('page_num')
        reviews = paginator.get_page(page_number)
        serializer = ReviewSerializer(reviews, many=True)
        data = serializer.data
        data.append({'total_pages': paginator.num_pages})
        return Response(data)
    
    # 리뷰 생성
    elif request.method == 'POST':
        print(request.data)
        serializer = ReviewSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
단일 리뷰 조회, 수정 및 삭제
'''
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def review_detail(request, movie_pk, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 단일 리뷰 조회
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 현재 유저와 리뷰를 쓴 유저가 같은 경우만 수정 및 삭제
    elif request.user == review.user:
    # 리뷰 수정
        if request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        # 리뷰 삭제
        elif request.method == 'DELETE':
            review.delete()
            data = {
                'delete' : f'{review_pk}번 리뷰가 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

'''
전체 댓글 조회 및 생성
'''
@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def comment_list(request, review_pk):
    # 현재 리뷰 가져오기
    review = get_object_or_404(Review, id=review_pk)
    # print(review.id)
    # print(request.user)
    # user = get_object_or_404(User, id=1)
    # 해당 리뷰의 댓글 조회
    print('aaa')
    print(request.user)
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk).order_by('-pk')
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    # 해당 리뷰의 댓글 작성
    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        # print(serializer)
        # print(request.user)
        if serializer.is_valid(raise_exception=True):
            # Vue에서 axios 요청할 때 URI에 movie의 id값을 넣어서 요청해야 함
            serializer.save(user=request.user, review=review)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

'''
상세 댓글 수정 및 삭제
'''
@api_view(['PUT', 'DELETE'])
@permission_classes([AllowAny])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, id=comment_pk)
    print(comment.user)
    print(request.user)

    # 현재 유저와 댓글 작성자가 같을 때 수정 및 삭제 가능
    if request.user == comment.user:
        # 수정
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        # 삭제
        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete' : f'{comment_pk}번 댓글이 삭제되었습니다.'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
        
    return Response({ 'Unauthorized': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

'''
개별 영화 장르 조회
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def genres (request, movie_pk):
    # 영화 선택
    movie = get_object_or_404(Movie, pk=movie_pk)
    movieserializer = MovieSerializer(movie)
    # 해당 영화에 포함되는 genre_id 저장(1~N개)
    movie_genres = movieserializer.data.get('genres')    

    # 저장된 리스트에 속하는 장르 objects get
    get_genres = Genre.objects.filter(id__in=movie_genres)
    serializer = GenreSerializer(get_genres, many=True)
    
    return Response(serializer.data)

'''
개별 영화 감독 조회
'''
@api_view(['GET'])
@permission_classes([AllowAny])
def director(request, movie_pk):
    get_movie = Movie.objects.get(pk=movie_pk)
    directors = get_movie.directors.all()
    serializer= DirectorSerializer(directors, many=True)
    return Response(serializer.data)

# 평점 매기는거는 나중에 
def voterate(request, movie_pk):
    pass


'''
나라별 랜덤 영화 조회
'''
import random
@api_view(['GET'])
# @permission_classes([AllowAny])
def randomMovie(request, country_name):
    # DB에서 랜덤하게 하나 뽑아줌!
    movie = Movie.objects.filter(country_name=country_name).order_by('?')[:1]
    # movie = random.sample(movies, 1)
    moviedata = serializers.serialize('json', movie)
    return HttpResponse(moviedata, content_type="text/json-comment-filtered")
