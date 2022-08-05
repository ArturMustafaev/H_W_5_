from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from main.models import Category, Product, Tag
from main.serializers import (ProductSerializer,
                              CategorySerializer,
                              ProductDetailSerializer,
                              ProductValidateSerializer)
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

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

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class CategoryItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

class CategoryAPIViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


@api_view(['GET', 'POST'])
def product_list_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        data = ProductSerializer(product, many=True).data
        return Response(data=data)
    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = request.data.get('name')
        text = request.data.get('text')
        price = request.data.get('price')
        category_id = request.data.get('category_id')
        product = Product.objects.create(
            title=name,
            descriptions=text,
            price=price,
            category_id=category_id
        )
        product.tags.set(serializer.validated_data['tags'])
        return Response(data=ProductSerializer(product).data)

@api_view(['GET', 'PUT', 'DELETE'])
def product_item_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ProductDetailSerializer(product).data
        return Response(data=data)
    elif request.method == 'DElETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = ProductValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                            data={'errors': serializer.errors})
        name = serializer.validated_data.get('name')
        text = serializer.validated_data.get('text')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        product.title = name
        product.descriptions = text
        product.price = price
        product.category_id = category_id
        product.save()
        return Response(data=ProductSerializer(product).data)


