from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published_year = models.IntegerField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='books')
    def __str__(self):
        return self.title
