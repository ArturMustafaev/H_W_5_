from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from main.models import Category, Product
from main.serializers import ProductSerializer, CategorySerializer, ProductDetailSerializer

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

# @api_view(['GET'])
# def categories_view(request):
#     categories = Category.objects.all()
#     data = CategorySerializer(categories, many=True).data
#     return Response(data=data)

@api_view(['GET'])
def product_list_view(request):
    product = Product.objects.all()
    data = ProductSerializer(product, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    data = ProductDetailSerializer(product).data
    return Response(data=data)
