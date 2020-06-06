from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='countries')

    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(max_length=128, unique=True)
    biography = models.TextField()
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f'{self.name}'


class Genre(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    name = models.CharField(max_length=128, unique=True)
    price = models.IntegerField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='authors')
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, related_name='genres')

    def __str__(self):
        return f'{self.name}'

