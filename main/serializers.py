from main.models import Category, Product, Review
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name'.split()

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = 'id product'.split()

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title decriptions price category reviews'.split()

class ProductDetailSerializer(serializers.ModelSerializer):
    filtered_reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        foelds = 'title decriptions price reviews filtered_reviews rating'.split()

    def get_filtered_reviews(self, product):
        reviews = Review.objects.filter(product=product, stars__gt=3)
        reviews = product.reviews.filter(stars__gt=3)
        return ReviewSerializer(reviews, many=True).data
