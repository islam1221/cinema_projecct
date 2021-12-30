from django.db.models import fields
from rest_framework import serializers
from .models import Movie, Reviews, Genres, Cinema

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','description','cinema','genres']

class CinemaReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class MovieDetailSerializers(serializers.ModelSerializer):
    genres = GenresSerializer(many = True)
    cinema = CinemaSerializer(many = False)

    class Meta:
        model = Movie
        fields = 'id title description cinema genres'.split()
    