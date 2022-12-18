"""
mikroways_prueba URL Configuration
"""
from django.contrib import admin
from django.urls import path

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from django.conf.urls import url
from django.urls import include

from rest_framework import permissions, routers
from car.api import CarViewSet

schema_view = get_schema_view(
    openapi.Info(
        title='Mikroways prueba API',
        default_version='v1',
        description='Documentacion Base de Mikroways',
        contact=openapi.Contact(email='marco.cristofano.dev@gmail.com'),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = 'api'
router = routers.SimpleRouter()

# Car App.
router.register(r'car', CarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'api/', include(router.urls)),
]
