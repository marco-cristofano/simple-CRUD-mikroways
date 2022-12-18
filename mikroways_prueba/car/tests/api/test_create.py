from rest_framework.test import APITestCase


class ApiCreateCar(APITestCase):
    url = '/api/car/'
    body = {
        'name': 'Delta Integrale',
        'brand': 'Lancia',
        'year': 1979
    }

    def test_retrieve_ok(self):
        response = self.client.post(self.url, self.body)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(len(response.data), 4)
        car = response.data
        self.assertEqual(car['name'], 'Delta Integrale')
        self.assertEqual(car['brand'], 'Lancia')
        self.assertEqual(car['year'], 1979)
        self.assertContains(response, 'id', status_code=201)


class ApiCreateFailCar(APITestCase):
    url = '/api/car/'
    body = {
        'name': 'Delta Integrale',
        'brand': 'Lancia',
        'year': 1979
    }

    def test_whitout_name(self):
        body = self.body.copy()
        body.pop('name')
        response = self.client.post(self.url, body)
        self.assertContains(response, 'name', status_code=400)

    def test_whitout_brand(self):
        body = self.body.copy()
        body.pop('brand')
        response = self.client.post(self.url, body)
        self.assertContains(response, 'brand', status_code=400)

    def test_whitout_year(self):
        body = self.body.copy()
        body.pop('year')
        response = self.client.post(self.url, body)
        self.assertContains(response, 'year', status_code=400)

    def test_negative_year(self):
        body = self.body.copy()
        body['year'] = '-1'
        response = self.client.post(self.url, body)
        self.assertContains(response, 'year', status_code=400)
