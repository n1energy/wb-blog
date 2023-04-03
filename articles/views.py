from django.shortcuts import render
from rest_framework import viewsets

from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
