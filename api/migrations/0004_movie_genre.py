# Generated by Django 2.2.3 on 2020-12-01 18:06

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_movie_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Unclassified', 'Unclassified'), ('Action', 'Action'), ('Adult', 'Adult'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ('Biography', 'Biography'), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Family', 'Family'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Game-Show', 'Game-Show'), ('History', 'History'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Music', 'Music'), ('Mystery', 'Mystery'), ('News', 'News'), ('Reality-TV', 'Reality-TV'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Short', 'Short'), ('Sport', 'Sport'), ('Talk-Show', 'Talk-Show'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], default='Unclassified', help_text='Género', max_length=232),
        ),
    ]
