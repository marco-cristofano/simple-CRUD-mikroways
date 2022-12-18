from rest_framework.test import APITestCase
from car.models import Car


class ApiPatchCar(APITestCase):
    url = '/api/car/'

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_patch_name(self):
        url = self.get_url(self.car.pk)
        body = {'name': 'Palio'}
        response = self.client.patch(url, body)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Palio')
        self.assertEqual(car['brand'], 'Lancia')
        self.assertEqual(car['year'], 1979)

    def test_patch_brand(self):
        url = self.get_url(self.car.pk)
        body = {'brand': 'Fiat'}
        response = self.client.patch(url, body)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Delta Integrale')
        self.assertEqual(car['brand'], 'Fiat')
        self.assertEqual(car['year'], 1979)

    def test_patch_year(self):
        url = self.get_url(self.car.pk)
        body = {'year': '1996'}
        response = self.client.patch(url, body)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Delta Integrale')
        self.assertEqual(car['brand'], 'Lancia')
        self.assertEqual(car['year'], 1996)


class ApiPatchFailCar(APITestCase):
    url = '/api/car/'

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_negative_year(self):
        url = self.get_url(self.car.pk)
        body = {'year': '-1'}
        response = self.client.patch(url, body)
        self.assertContains(response, 'year', status_code=400)
