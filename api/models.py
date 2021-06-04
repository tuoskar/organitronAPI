from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField  # Así podemos hacer selección múltiple de elecciones




# Create your models here.
# Movie model

class Movie(models.Model):

    # genre choices declarations for multi choosing on cascade menu
    UNCLASSIFIED = 'Unclassified'
    ACTION = 'Action'
    ADULT = 'Adult'
    ADVENTURE = 'Adventure'
    ANIMATION = 'Animation'
    BIOGRAPHY = 'Biography'
    COMEDY = 'Comedy'
    CRIME = 'Crime'
    DOCUMENTARY = 'Documentary'
    DRAMA = 'Drama'
    FAMILY = 'Family'
    FANTASY = 'Fantasy'
    FILM_NOIR = 'Film-Noir'
    GAME_SHOW = 'Game-Show'
    HISTORY = 'History'
    HORROR = 'Horror'
    MUSICAL = 'Musical'
    MUSIC = 'Music'
    MYSTERY = 'Mystery'
    NEWS = 'News'
    REALITY_TV = 'Reality-TV'
    ROMANCE = 'Romance'
    SCI_FI = 'Sci-Fi'
    SHORT = 'Short'
    SPORT = 'Sport'
    TALK_SHOW = 'Talk-Show'
    THRILLER = 'Thriller'
    WAR = 'War'
    WESTERN = 'Western'

    GENRE_CHOICES = [
        (UNCLASSIFIED, 'Unclassified'),
        (ACTION, 'Action'),
        (ADULT, 'Adult'),
        (ADVENTURE, 'Adventure'),
        (ANIMATION, 'Animation'),
        (BIOGRAPHY, 'Biography'),
        (COMEDY, 'Comedy'),
        (CRIME, 'Crime'),
        (DOCUMENTARY, 'Documentary'),
        (DRAMA, 'Drama'),
        (FAMILY, 'Family'),
        (FANTASY, 'Fantasy'),
        (FILM_NOIR, 'Film-Noir'),
        (GAME_SHOW, 'Game-Show'),
        (HISTORY, 'History'),
        (HORROR, 'Horror'),
        (MUSICAL, 'Musical'),
        (MUSIC, 'Music'),
        (MYSTERY, 'Mystery'),
        (NEWS, 'News'),
        (REALITY_TV, 'Reality-TV'),
        (ROMANCE, 'Romance'),
        (SCI_FI, 'Sci-Fi'),
        (SHORT, 'Short'),
        (SPORT, 'Sport'),
        (TALK_SHOW, 'Talk-Show'),
        (THRILLER, 'Thriller'),
        (WAR, 'War'),
        (WESTERN, 'Western'),
    ]


    # video_quality choices declarations for choosing on cascade menu
    SCREENER = 'Screener'
    DVD_RIP = 'DVD Rip'
    HD_RIP = 'HD Rip'
    HD_TV_720 = 'HD TV 720p'
    BR_RIP = 'BR Rip'
    MICRO_HD_720 = 'Micro HD 720p'
    MICRO_HD = 'Micro HD 1080p'
    BLURAY_1080 = 'BluRay 1080p'
    BDREMUX_1080 = 'BluRay Dremux 1080p'
    UHD_4K = '4K' 

    VIDEO_QUALITY_CHOICES = [
        (SCREENER, 'Screener (Calidad baja)'),
        (DVD_RIP, 'DVD Rip (Calidad baja)'),
        (HD_RIP, 'HD Rip (Calidad media)'),
        (HD_TV_720, 'HD TV 720p (Calidad media)'),
        (BR_RIP, 'BR Rip (Calidad media)'),
        (MICRO_HD_720, 'Micro HD 720p (Calidad media/alta)'),
        (MICRO_HD, 'Micro HD 1080p (Calidad alta)'),
        (BLURAY_1080, 'BluRay 1080p (Calidad alta)'),
        (BDREMUX_1080, 'BluRay Dremux 1080p (Calidad alta)'),
        (UHD_4K , '4K (Calidad muy alta)'),
    ]

    GENRES_CHOICE_GUIDE = ' Opciones de género: Unclassified, Action, Adult, Adventure, Animation, Biography, Comedy, Crime, Documentary, Drama, Family, Fantasy, Film-Noir, Game-Show, History, Horror, Musical, Music, Mystery, News, Reality-TV, Romance, Sci-Fi, Short, Sport, Talk-Show, Thriller, War, Western'
    
    

    title = models.CharField(max_length=150)
    release_date = models.IntegerField(default=2000)
    image = models.URLField(help_text="URL de imdb o Joblo.com")
    synopsis = models.TextField(help_text="Argumento de la película")
    imdb_score = models.FloatField()
    imdb_link = models.URLField(help_text="URL link de imdb")
    #genre = MultiSelectField(choices=GENRE_CHOICES, default=UNCLASSIFIED, help_text="Género")#, blank=True, null=True)
    genre = models.CharField( help_text=GENRES_CHOICE_GUIDE, max_length=150)#, blank=True, null=True)
    #genre_2 = MultiSelectField(choices=GENRE_CHOICES, default=UNCLASSIFIED, help_text="Género 2", blank=True, null=True)
    #genre_3 = MultiSelectField(choices=GENRE_CHOICES, default=UNCLASSIFIED, help_text="Género 3", blank=True, null=True)
    #genre_4 = MultiSelectField(choices=GENRE_CHOICES, default=UNCLASSIFIED, help_text="Género 4", blank=True, null=True)
    duration = models.CharField(help_text="Formato de duración: Xh XXmin", max_length=10, default="0h 00min")
    video_quality = models.CharField(max_length=150, choices=VIDEO_QUALITY_CHOICES)
    movie_location = models.CharField(max_length=150, help_text="En que disco duro está almacenada la película")
    favourites = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']


class FavouriteMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class SeenMovie(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


class ToSeeMovie(models.Model):
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)


from django.db.models.signals import post_save, post_delete

def update_favourites(sender, instance, **kwargs):
    count = instance.movie.favouritemovie_set.all().count()
    instance.movie.favourites = count
    instance.movie.save()

# En el post_delete se pasa la copia de la instance que ya no existe
# In the post_delete we pass the copy of the instance that no longer exists
post_save.connect(update_favourites, sender=FavouriteMovie)
post_delete.connect(update_favourites, sender=FavouriteMovie)
