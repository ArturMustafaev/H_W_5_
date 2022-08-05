from rest_framework import serializers
from movie_app.models import Review, Movie, Director


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = 'all'.split()


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()


# class MovieValidateSerializer(serializers.Serializer):
#     title = serializers.CharField(min_length=3, max_length=100)
#     text = serializers.CharField(required=False)
#     director = serializers.CharField(min_length=5)