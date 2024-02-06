from django.db import models

from embed_video.fields import EmbedVideoField

# Create your models here.
class Movie(models.Model):
    GENRE = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Sports', 'Sports'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Movie/image')
    cast = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length = 300)
    director = models.CharField(max_length=150, null=True)
    genre = models.CharField(max_length=200, null=True, choices=GENRE)
    quantity = models.FloatField(null=True)
    price = models.FloatField(null=True)
    url = EmbedVideoField(null=True)

    def __str__(self):
        return self.title

class Reserve(models.Model):
    GENRE = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Fantasy', 'Fantasy'),
        ('Horror', 'Horror'),
        ('Musical', 'Musical'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Sports', 'Sports'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),
    )
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='Movie/image')
    cast = models.CharField(max_length=300, null=True)
    description = models.CharField(max_length = 300)
    director = models.CharField(max_length=150, null=True)
    genre = models.CharField(max_length=200, null=True, choices=GENRE)
    quantity = models.FloatField(null=True)
    price = models.FloatField(null=True)
    url = EmbedVideoField(null=True)

    def __str__(self):
        return self.title
