from rest_framework.viewsets import ModelViewSet

from .models import Book, Country, City, Author, Genre
from .serializers import BookSerializer, CountrySerializer, CitySerializer, GenreSerializer, AuthorSerializer


class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class BookViewSet(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
