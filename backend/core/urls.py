from rest_framework.routers import DefaultRouter
from .views import BookViewSet, CountryViewSet, CityViewSet, AuthorViewSet, GenreViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('countries', CountryViewSet)
router.register('cities', CityViewSet)
router.register('genres', GenreViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = router.urls
