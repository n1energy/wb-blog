from requests import Response
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from articles.serializers import ArticleSerializer, ReadArticleSerializer
from django.contrib.auth.models import User

from articles.models import Article, ReadArticle
from users.models import SubscribtionUser


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created", "updated"]
    ordering = ["-created"]

    @action(detail=False, permission_classes=[IsAuthenticated])
    def feed(self, request, *args, **kwargs):
        user_follow_id = SubscribtionUser.objects.filter(subscriber_id=self.request.user).values_list('user_id',
                                                                                                      flat=True)
        queryset = Article.objects.filter(user__in=user_follow_id)
        # response = super().list(self, request, *args, **kwargs)
        # return response
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthenticated])
    def feed_read(self, request, *args, **kwargs):
        pass

    # def get_queryset(self):
    #     user_follow_id = SubscribtionUser.objects.filter(subscriber=self.request.user)
    #     qs = Article.objects.filter(user__in=user_follow_id)
    #     return qs

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def MarkRead(self, request, *args, **kwargs):
        # obj = 
        pass


class ReadArticleViewSet(mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = ReadArticle.objects.all()
    serializer_class = ReadArticleSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'article'

    def get_object(self):
        obj, _ = ReadArticle.objects.get_or_create(user=self.request.user, article_id=self.kwargs['article'])
        return obj
