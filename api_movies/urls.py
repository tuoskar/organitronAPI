"""api_movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from api import views
from rest_framework import routers

router = routers.DefaultRouter()

# En el router vamos añadiendo los endpoints a los viewsets
# In router we add the endpoints to the viewsets
router.register('movies', views.MovieViewSet, basename='Movies')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/favourite/', views.MarkFavouriteMovie.as_view()),
    path('api/v1/favourites/', views.ListFavouriteMovies.as_view()),
    path('api/v1/seen/', views.MarkSeenMovie.as_view()),
    path('api/v1/seen_movies/',views.ListSeenMovies.as_view()),
    path('api/v1/to_see/', views.MarkToSeeMovie.as_view()),
    path('api/v1/watchlist/', views.ListToSeeMovies.as_view()),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_auth.urls')),
    path('api/v1/auth/registration/', include('rest_auth.registration.urls')),
]
