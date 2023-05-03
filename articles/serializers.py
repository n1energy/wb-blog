from rest_framework import serializers

from articles.models import Article, ReadArticle


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ("id", "user", "title", "body", "created", "updated")
        read_only_fields = ["user"]


class ReadArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadArticle
        fields = ("user", "article", "is_read")
