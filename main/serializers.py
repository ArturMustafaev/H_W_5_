from rest_framework import serializers
from main.models import Category, Product, Review
from rest_framework.exceptions import ValidationError

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id'.split()

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title descriptions price category reviews'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'title price reviews filtered_reviews rating'.split()

    def get_filtered_reviews(self, product):
        reviews = Review.objects.filter(product=product, stars__gt=3)
        reviews = product.reviews.filter(stars__gt=3)
        return ReviewSerializer(reviews, many=True).data

class ObjectSerializer(serializers.Serializer):
    key = serializers.CharField()
    key2 = serializers.IntegerField()

class ProductValidateSerializer(serializers.Serializer):
    name = serializers.CharField(min_length=3, max_length=100)
    text = serializers.CharField(required=False)
    price = serializers.FloatField(min_value=0.1)
    category_id = serializers.IntegerField(min_value=1)
    tags = serializers.ListField(child=serializers.IntegerField())
    object = ObjectSerializer()

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError('Category does not exists!')
        return category_id

    def validate_name(self, name):
        products = Product.objects.filter(title=name)
        if products.count()>0:
            raise ValidationError('Product must be unique!')
        return name