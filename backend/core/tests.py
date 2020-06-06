import json

from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from .models import Country, City, Genre
from .serializers import CountrySerializer


class CountriesTestCase(APITestCase):

    def setUp(self):
        Country.objects.create(name="123")

    def test_posting(self):
        data = {"name": 'asd'}
        response = self.client.post("/api/v1/countries/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getting(self):
        response = self.client.get("/api/v1/countries/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getting_detail(self):
        response = self.client.get("/api/v1/countries/1/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GenresTestCase(APITestCase):

    def test_posting(self):
        data = {"name": 'asd'}
        response = self.client.post("/api/v1/genres/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_getting(self):
        response = self.client.get("/api/v1/genres/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
