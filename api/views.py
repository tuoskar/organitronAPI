#from django.shortcuts import render
from .models import Movie, FavouriteMovie, SeenMovie, ToSeeMovie
from .serializers import MovieSerializer, FavouriteMovieSerializer, SeenMovieSerializer, ToSeeMovieSerializer

from django.shortcuts import get_object_or_404

from django_filters.rest_framework import DjangoFilterBackend # Para filtrar dentro de un atirbuto(genero) / Used for filtering inside atribute (genre)

from rest_framework import viewsets, views, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ['title', 'release_date', 'genre']
    ordering_fields = ['favourites', 'release_date', 'imdb_score', 'created', 'genre', 'title', 'duration', 'id']
    filterset_fields = {
            'genre': ['contains'],
            'title': ['contains'],
            'id': ['exact']
        }# 'id', 'release_date',]
    #filterset_fields = ['favourites']

# Vistas para marcar peliculas/Views to mark movies
class MarkFavouriteMovie(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # POST  -> Se usa para crear un recurso -/- Is used for creating a resource
    # PUT -> Se usa para modificar/actualizar un recurso -/- Is used to modify or update a resource

    def post(self, request):

        movie = get_object_or_404(
            Movie, id=self.request.data.get('id', 0)
        )

        favourite, created = FavouriteMovie.objects.get_or_create(
            movie=movie, user=request.user
        )

        # Por defecto suponemos que se crea bien / By default we asume it creates fine
        content = {
            'id': movie.id,
            'favourite': True
        }

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        # If it's not created is because already exists, then we delete the favourite
        if not created:
            favourite.delete()
            content['favourite'] = False

        return Response(content)


class MarkSeenMovie(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # POST  -> Se usa para crear un recurso -/- Is used for creating a resource
    # PUT -> Se usa para modificar/actualizar un recurso -/- Is used to modify or update a resource

    def post(self, request):

        movie = get_object_or_404(
            Movie, id=self.request.data.get('id', 0)
        )

        seen, created = SeenMovie.objects.get_or_create(
            movie=movie, user=request.user
        )

        # Por defecto suponemos que se crea bien / By default we asume it creates fine
        content = {
            'id': movie.id,
            'seen': True
        }

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        # If it's not created is because already exists, then we delete the favourite
        if not created:
            seen.delete()
            content['seen'] = False

        return Response(content)


class MarkToSeeMovie(views.APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # POST  -> Se usa para crear un recurso -/- Is used for creating a resource
    # PUT -> Se usa para modificar/actualizar un recurso -/- Is used to modify or update a resource

    def post(self, request):

        movie = get_object_or_404(
            Movie, id=self.request.data.get('id', 0)
        )

        to_see, created = ToSeeMovie.objects.get_or_create(
            movie=movie, user=request.user
        )

        # Por defecto suponemos que se crea bien / By default we asume it creates fine
        content = {
            'id': movie.id,
            'to_see': True
        }

        # Si no se ha creado es que ya existe, entonces borramos el favorito
        # If it's not created is because already exists, then we delete the favourite
        if not created:
            to_see.delete()
            content['to_see'] = False

        return Response(content)


# Vistas para listar peliculas/Views to list movies
class ListFavouriteMovies(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET -> Se usa para hacer lecturas/Is used to make readings

    def get(self, request):

        favourite_movies = FavouriteMovie.objects.filter(
            user=request.user)
        serializer = FavouriteMovieSerializer(
            favourite_movies, many=True)

        return Response(serializer.data)


class ListSeenMovies(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET -> Se usa para hacer lecturas/Is used to make readings

    def get(self, request):

        seen_movies = SeenMovie.objects.filter(
            user=request.user)
        serializer = SeenMovieSerializer(
            seen_movies, many=True)

        return Response(serializer.data)


class ListToSeeMovies(views.APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # GET -> Se usa para hacer lecturas/Is used to make readings

    def get(self, request):

        to_see_movies = ToSeeMovie.objects.filter(
            user=request.user)
        serializer = ToSeeMovieSerializer(
            to_see_movies, many=True)

        return Response(serializer.data)
