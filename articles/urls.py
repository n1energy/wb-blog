from django.urls import include, path
from rest_framework.routers import DefaultRouter

from articles.views import ArticleViewSet

router = DefaultRouter()
#
router.register('users', ArticleViewSet, basename='articles')
urlpatterns = [
    path('', include(router.urls))
]
