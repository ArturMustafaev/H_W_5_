from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.serializer import ReviewSerializer, DirectorSerializer
from movie_app.models import Review, Director

# Create your views here.

@api_view(['GET'])
def director(request):
    context = {
        'list': [
            'Роберт Эггерс',
            'Дэмиен Шазелл',
        ]
    }

    return Response(data=context, status=200)

@api_view(['GET'])
def movie(request):
    context = {
        'title': [
            'The Green Mile',
            'Schindler list',
        ]
    }

    return Response(data=context, status=200)

@api_view(['GET'])
def review(request):
    context = {
        'text': [
            'Хороший фильм!',
            'Ужасный фильм',
        ]
    }

    return Response(data=context, status=200)

@api_view(['GET'])
def review_list_view(request):
    reviews = Review.objects.all()
    data = ReviewSerializer(reviews, many=True).data
    return Response(data=data)

@api_view(['GET'])
def director_list(request):
    director = Director.objects.all()
    data = DirectorSerializer(director, many=True).data
    return Response(data=data)