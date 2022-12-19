from django.contrib.auth.models import User
from car.models import Car
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from django.contrib.auth.models import Group


from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Create users'

    def handle(self, *args, **options):
        try:
            if not User.objects.filter(username='common__user').exists():
                User.objects.create_user(
                    username='common__user',
                    password='1234')
            if not User.objects.filter(username='privileged__user').exists():
                privileged_user = User.objects.create_user(
                    username='privileged__user',
                    password='1234')
                content_type = ContentType.objects.get_for_model(Car)
                permission = Permission.objects.get_or_create(
                    codename='can_delete_all_whit_permission',
                    name='can_delete_all_whit_permission',
                    content_type=content_type,
                )[0]
                group = Group.objects.get_or_create(name='admin_deletes')[0]
                group.permissions.add(permission)
                privileged_user.groups.add(group)
        except Exception as e:
            raise CommandError('Initalization failed. Error', e)
