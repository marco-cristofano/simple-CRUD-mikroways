from rest_framework.test import APITestCase
from car.models import Car


class ApiUpdateCar(APITestCase):
    url = '/api/car/'
    body = {
        'name': 'Palio',
        'brand': 'Fiat',
        'year': 1996
    }

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_update_ok(self):
        url = self.get_url(self.car.pk)
        response = self.client.put(url, self.body)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Palio')
        self.assertEqual(car['brand'], 'Fiat')
        self.assertEqual(car['year'], 1996)


class ApiUpdateFailCar(APITestCase):
    url = '/api/car/'
    body = {
        'name': 'Palio',
        'brand': 'Fiat',
        'year': 1996
    }

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_whitout_name(self):
        url = self.get_url(self.car.pk)
        body = self.body
        body.pop('name')
        response = self.client.put(url, body)
        self.assertContains(response, 'name', status_code=400)

    def test_whitout_brand(self):
        url = self.get_url(self.car.pk)
        body = self.body
        body.pop('brand')
        response = self.client.put(url, body)
        self.assertContains(response, 'brand', status_code=400)

    def test_whitout_year(self):
        url = self.get_url(self.car.pk)
        body = self.body
        body.pop('year')
        response = self.client.put(url, body)
        self.assertContains(response, 'year', status_code=400)

    def test_negative_year(self):
        url = self.get_url(self.car.pk)
        body = self.body
        body['year'] = '-1'
        response = self.client.put(url, body)
        self.assertContains(response, 'year', status_code=400)
