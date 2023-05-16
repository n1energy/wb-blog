import json

from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from articles.models import Article
from django.contrib.auth.models import User

from rest_framework.views import status

from users.serializers import UserSerializer


class UserApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username="alex", password="wbtest")
        self.user_2 = User.objects.create(username="murfy", password="wbtest")

        self.article_1 = Article.objects.create(
            title="Test_article_1", body="hello_1", user=self.user_1
        )
        self.article_2 = Article.objects.create(
            title="Test_article_2", body="hello_2", user=self.user_1
        )
        self.article_3 = Article.objects.create(
            title="Test_article_3", body="hello_3", user=self.user_2
        )


def test_list_users(self):
    url = reverse("users-list")
    response = self.client.get(url)
    articles = Article.objects.all().order_by("-created")
    serializer_data = UserSerializer(articles, many=True).data
    self.assertEqual(serializer_data, response.data.get("results"))
    self.assertEqual(2, User.objects.all().count())
    self.assertEqual(status.HTTP_200_OK, response.status_code)