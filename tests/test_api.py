import json
from django.urls import reverse
from articles.models import Article
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework.views import status



class BooksApiTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create(username="alex")
        self.user_2 = User.objects.create(username="murfy")

        self.article_1 = Article.objects.create(title="Test_article_1",body="hello_1",
                                          user= self.user_1)
        self.article_2 = Article.objects.create(name="Test_article_2", body="hello_2",
                                          user= self.user_1)
        self.article_3 = Article.objects.create(name="Test_article_3", body="hello_3",
                                          user= self.user_2)
        # RelationUserBook.objects.create(user=self.user, book=self.book_1, like=True, rating=5)

    def test_get(self):
        pass
        # url = reverse("articles")
        # response = self.client.

    def test_create(self):
        self.assertEqual(3, Article.objects.all().count())
        url = reverse('articles')
        data = {
            "title": "Python 310",
            "body": "new release!",
            "user": self.user_2
        }
        self.client.force_login(self.user)
        json_data = json.dumps(data)
        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(4, Article.objects.all().count())
        self.assertEqual(Article.objects.last().master, self.user_2)