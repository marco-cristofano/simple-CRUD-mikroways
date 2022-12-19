from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from car.models import Car
from rest_framework.authtoken.models import Token


class ApiAllDeleteCar(APITestCase):
    url = '/api/car/all_delete/'

    def setUp(self):
        Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )
        Car.objects.create(
            name='Palio',
            brand='Fiat',
            year=1996
        )

    def test_without_credentials(self):
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 401)

    def test_ok(self):
        user = User.objects.create(username='admin')
        Token.objects.get_or_create(user=user)
        self.client.force_authenticate(user=user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Car.objects.count(), 0)

