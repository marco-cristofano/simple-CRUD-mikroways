from rest_framework.test import APITestCase
from car.models import Car


class ApiDeleteCar(APITestCase):
    url = '/api/car/'

    def setUp(self):
        self.car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )

    def get_url(self, id):
        return self.url + str(id) + '/'

    def test_delete_ok(self):
        url = self.get_url(self.car.pk)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Car.objects.count(), 0)
        self.assertEqual(Car.all_objects.count(), 1)
