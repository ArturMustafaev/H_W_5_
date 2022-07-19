from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def test_view(request):
    context = {
        'text': 'Hello world!!!',
        'integer': 100,
        'float': 99.9,
        'boolean': True,
        'list': [1, 2, 3],
        'dict': {'key', 'value'},
        'list_of_dict': [
            {'key', 'value'},
            {'key', 'value'},
            {'key', 'value'},
        ]
    }
    return Response(data=context, status=status.HTTP_200_OK)

@api_view(['GET'])
def categories_view(request):
    return Response()