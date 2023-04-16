from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from articles.models import Article, ReadedArticle
from articles.serializers import ArticleSerializer, ReadArticleSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [OrderingFilter]
    ordering_fields = ["created", "updated"]
    ordering = ["-created"]
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())
    # @action(detail=True, method=[POST])
    def MarkRead(self, request, *args, **kwargs):
        # obj = 
        pass
    
class ReadArticleViewSet(viewsets.ModelViewSet):
    queryset = ReadedArticle.objects.all()
    serializer_class = ReadArticleSerializer
    # permission_classes = [IsAuthenticated]

# class ReadArticleViewSet(APIview):
