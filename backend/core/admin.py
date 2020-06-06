from django.contrib import admin

from .models import Book, Author, City, Country, Genre

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(Genre)
