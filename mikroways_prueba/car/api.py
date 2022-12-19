from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import (
    permissions,
    viewsets,
    status
)

from car import documentation as DOC
from car.serializers import CarSerializer
from car.models import Car
from car.permissions import CarPermissions


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('name')
    serializer_class = CarSerializer

    @swagger_auto_schema(**DOC.list_car)
    def list(self, request):
        return super().list(request)

    @swagger_auto_schema(**DOC.retrieve)
    def retrieve(self, request, pk=None):
        return super().retrieve(request, pk)

    @swagger_auto_schema(**DOC.create)
    def create(self, request):
        return super().create(request)

    @swagger_auto_schema(**DOC.delete)
    def delete(self, request, pk=None):
        return super().delete(request, pk)

    @swagger_auto_schema(**DOC.delete_all)
    @action(
        detail=False,
        methods=['delete'],
        url_path='all_delete',
        permission_classes=[permissions.IsAuthenticated, CarPermissions]
    )
    def all_delete(self, request):
        Car.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @swagger_auto_schema(**DOC.delete_all_with_permission)
    @action(
        detail=False,
        methods=['delete'],
        url_path='all_delete_with_permission',
        permission_classes=[permissions.IsAuthenticated, CarPermissions]
    )
    def all_delete_with_permission(self, request):
        Car.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
