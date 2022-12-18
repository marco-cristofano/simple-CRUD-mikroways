from django.test import TestCase
from car.models import Car


class CarModelStrTest(TestCase):

    def test_str(self):
        car = Car.objects.create(
            name='Delta Integrale',
            brand='Lancia',
            year=1979
        )
        self.assertEqual(car.__str__(), 'Delta Integrale - Lancia (1979)')
