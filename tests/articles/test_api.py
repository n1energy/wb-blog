import json
from django.urls import reverse

from rest_framework.test import APITestCase

from articles.models import Article
from django.contrib.auth.models import User

from rest_framework.views import status
from rest_framework_simplejwt.tokens import RefreshToken
from articles.serializers import ArticleSerializer


class UserApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create(username="alex", password="wbtest")
        self.user_2 = User.objects.create(username="murfy", password="wbtest")


class ArticlesApiTestCase(APITestCase):
    def setUp(self):
        self.user_1 = User.objects.create_user(username="alex", password="wbblog")
        self.user_2 = User.objects.create_user(username="murfy", password="wbblog")

        self.article_1 = Article.objects.create(
            title="Test_article_1", body="hello_1", user=self.user_1
        )
        self.article_2 = Article.objects.create(
            title="Test_article_2", body="hello_2", user=self.user_1
        )
        self.article_3 = Article.objects.create(
            title="Test_article_3", body="hello_3", user=self.user_2
        )
        # RelationUserBook.objects.create(user=self.user, book=self.book_1, like=True, rating=5)
    # @property
    # def bearer_token(user):
    #     refresh = RefreshToken.for_user(user)
    #     return {"HTTP_AUTHORIZATION":f'Bearer {refresh.access_token}'}
    @classmethod
    def bearer_token(user):
        # assuming there is a user in User model
        user1 = User.objects.create_user(
            username='test@user.me', password='12345678'
        )
        refresh = RefreshToken.for_user(user)
        return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}

    
    # def test_get(self):
    #     url = reverse("articles-list")
    #     response = self.client.get(url)
    #     articles = Article.objects.all()
    #     serializer_data = ArticleSerializer(articles, many=True).data
    #     # self.assertEqual(serializer_data, response.data)
    #     self.assertEqual(3, Article.objects.all().count())
    #     self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_create(self):
        self.assertEqual(3, Article.objects.all().count())
        url = reverse("articles-list")
        data = {"title": "Python 310", "body": "new release!"}
        json_data = json.dumps(data)

        print(self.bearer_token(self.user_1))
        response = self.client.post(
            # url, data=json_data, content_type="application/json", **{"HTTP_AUTHORIZATION": self.create_jwt_token(self.user_1)})
            url, data=json_data, content_type="application/json", **self.bearer_token(self.user_1))
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Article.objects.all().count())
        # self.assertEqual(Article.objects.last().master, self.user_2)
