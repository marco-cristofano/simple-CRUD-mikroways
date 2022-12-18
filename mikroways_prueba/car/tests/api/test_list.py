from rest_framework.test import APITestCase
from car.models import Car


class ApiListCar(APITestCase):
    url = '/api/car/'

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

    def test_list_ok(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        car_1 = response.data[0]
        self.assertEqual(car_1['name'], 'Delta Integrale')
        self.assertEqual(car_1['brand'], 'Lancia')
        self.assertEqual(car_1['year'], 1979)

    def test_list_order(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        car_1 = response.data[0]
        self.assertEqual(car_1['name'], 'Delta Integrale')
        car_2 = response.data[1]
        self.assertEqual(car_2['name'], 'Palio')
