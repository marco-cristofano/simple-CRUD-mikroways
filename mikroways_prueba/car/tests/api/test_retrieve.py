from rest_framework.test import APITestCase
from car.models import Car


class ApiRetrieveCar(APITestCase):
    url = '/api/car/'

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_retrieve_ok(self):
        url = self.get_url(self.car.pk)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Delta Integrale')
        self.assertEqual(car['brand'], 'Lancia')
        self.assertEqual(car['year'], 1979)
