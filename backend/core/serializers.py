from rest_framework.serializers import ModelSerializer

from .models import Book, Country, City, Author, Genre


class CountrySerializer(ModelSerializer):

    class Meta:
        model = Country
        fields = ['id', 'name']


class CitySerializer(ModelSerializer):

    class Meta:
        model = City
        fields = ['id', 'name', 'country']


class AuthorSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'name', 'biography', 'city']


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'price', 'description', 'genre', 'author']
