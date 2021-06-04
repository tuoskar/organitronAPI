# Generated by Django 2.2.3 on 2020-10-28 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('release_date', models.IntegerField(default=2000)),
                ('image', models.URLField(help_text='URL de imdb')),
                ('synopsis', models.TextField(help_text='Argumento de la película')),
                ('imdb_score', models.FloatField()),
                ('imdb_link', models.URLField(help_text='URL link de imdb')),
                ('video_quality', models.CharField(choices=[('Screener', 'Screener (Calidad baja)'), ('DVD Rip', 'DVD Rip (Calidad baja)'), ('HD Rip', 'HD Rip (Calidad media)'), ('HD TV 720p', 'HD TV 720p (Calidad media)'), ('BR Rip', 'BR Rip (Calidad media)'), ('Micro HD 1080p', 'Micro HD 1080p (Calidad alta)'), ('BluRay 1080p', 'BluRay 1080p (Calidad alta)'), ('BluRay Dremux 1080p', 'BluRay Dremux 1080p (Calidad alta)'), ('4K', '4K (Calidad muy alta)')], max_length=150)),
                ('movie_location', models.CharField(max_length=150)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]