from movie_app.models import Review, Movie, Director
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'title'.split()

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer()
    class Meta:
        model = Review
        fields = 'text stars movie rating'.split()

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name'.split()

