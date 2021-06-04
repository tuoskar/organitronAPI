from .models import Movie, FavouriteMovie, SeenMovie, ToSeeMovie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        #fields = ['id', 'title', 'release', 'image', 'genre', 'synopsis',
                #'imdb_score', 'imdb_link', 'video_quality', 'movie_location',
                #'created', 'updated']
        fields = '__all__'


class FavouriteMovieSerializer(serializers.ModelSerializer):

    movie = MovieSerializer()

    class Meta:
        model = FavouriteMovie
        fields = ['movie']


class SeenMovieSerializer(serializers.ModelSerializer):

    movie = MovieSerializer()

    class Meta:
        model = FavouriteMovie
        fields = ['movie']


class ToSeeMovieSerializer(serializers.ModelSerializer):

    movie = MovieSerializer()

    class Meta:
        model = FavouriteMovie
        fields = ['movie']
