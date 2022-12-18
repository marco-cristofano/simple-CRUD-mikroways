from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets

from car.serializers import CarSerializer
from car.models import Car


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('name')
    serializer_class = CarSerializer
