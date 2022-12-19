from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class LoginGetTest(APITestCase):
    url = '/login/'
    credenciales = {
        'user': 'admin',
        'password': 'admin'
    }

    def test_login_405(self):
        response = self.client.get(self.url, self.credenciales)
        self.assertEqual(response.status_code, 405)


class LoginTest(APITestCase):
    url = '/login/'
    credenciales = {
        'user': 'admin',
        'password': '1234'
    }

    def setUp(self):
        User.objects.create_user(
            username='admin',
            password='1234'
        )

    def test_login_ok(self):
        response = self.client.post(self.url, self.credenciales)
        self.assertContains(response, 'token', 1, status_code=201)

    def test_login_bad_user(self):
        credenciales = self.credenciales.copy()
        credenciales['user'] = 'user'
        response = self.client.post(self.url, credenciales)
        self.assertContains(
            response, 'Credenciales inválidas', status_code=400)

    def test_login_bad_password(self):
        credenciales = self.credenciales.copy()
        credenciales['password'] = 'password'
        response = self.client.post(self.url, credenciales)
        self.assertContains(
            response, 'Credenciales inválidas', status_code=400)

    def test_without_user(self):
        credenciales = {'password': 'password'}
        response = self.client.post(self.url, credenciales)
        self.assertContains(response, 'user', status_code=400)

    def test_without_password(self):
        credenciales = {'user': 'user'}
        response = self.client.post(self.url, credenciales)
        self.assertContains(response, 'password', status_code=400)
