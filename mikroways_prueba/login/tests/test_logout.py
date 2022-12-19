from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token


class LoginTest(APITestCase):
    url = '/logout/'

    def setUp(self):
        user = User.objects.create_user(
            username='admin',
            password='1234'
        )
        Token.objects.get_or_create(user=user)[0]

    def test_logout_ok(self):
        user = User.objects.get(username='admin')
        self.client.force_authenticate(user=user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
