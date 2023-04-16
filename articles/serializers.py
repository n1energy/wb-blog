from rest_framework import serializers

from articles.models import Article, ReadedArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "user", "title", "body", "created", "updated")

class ReadArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadedArticle
        fields = ("article", "is_readed")
        