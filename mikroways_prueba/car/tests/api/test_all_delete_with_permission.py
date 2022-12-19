from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from car.models import Car
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import Group


class ApiAllDeleteWhitPermissionCar(APITestCase):
    url = '/api/car/all_delete_with_permission/'

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

    def test_without_permissions(self):
        user = User.objects.create(username='admin')
        Token.objects.get_or_create(user=user)
        self.client.force_authenticate(user=user)
        response = self.client.delete(self.url)
        self.assertContains(response, 'not have permission', status_code=403)

    def test_ok(self):
        user = User.objects.create(username='admin')
        Token.objects.get_or_create(user=user)
        self.client.force_authenticate(user=user)
        content_type = ContentType.objects.get_for_model(Car)
        permission = Permission.objects.create(
            codename='can_delete_all_whit_permission',
            name='can_delete_all_whit_permission',
            content_type=content_type,
        )
        group = Group.objects.create(name='admin_deletes')
        group.permissions.add(permission)
        user.groups.add(group)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Car.objects.count(), 0)
