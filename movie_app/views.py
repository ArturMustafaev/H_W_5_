from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import ReviewSerializer, DirectorSerializer, MovieSerializer
from movie_app.models import Review, Director, Movie
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination

# Create your views here.

@api_view(['GET', 'POST'])
def director(request):
    if request.method == 'GET':
        director = Director.objects.all()
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data=DirectorSerializer(director).data)


class DirectorAPIViewSet(ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    pagination_class = PageNumberPagination


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movie = Movie.objects.all()
#         data = MovieSerializer(movie, many=True).data
#         return Response(data=data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response()


class MovieAPIViewSet(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def review(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.method.get('stars')
        movie = request.method.get('movie')
        review = Review.objects.create(
            text=text,
            stars=stars,
            movie=movie
        )
        return Response(data=ReviewSerializer(review).data)



@api_view(['GET', 'POST'])
def review_list_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        data = ReviewSerializer(review, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        text = request.data.get('text')
        stars = request.method.get('stars')
        movie = request.method.get('movie')
        review = Review.objects.create(
            text=text,
            stars=stars,
            movie=movie
        )
        return Response(data=ReviewSerializer(review).data)


class ReviewAPIViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'PUT', 'DELETE'])
def director_list(request):
    director = Director.objects.all()
    if request.method == 'GET':
        data = DirectorSerializer(director, many=True).data
        return Response(data=data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        name = request.data.get('name')
        Director.name = name
        return Response(data=DirectorSerializer(director).data)