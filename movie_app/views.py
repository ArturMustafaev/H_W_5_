from rest_framework.decorators import api_view
from rest_framework.response import Response

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
