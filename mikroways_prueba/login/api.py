from rest_framework import (
    permissions,
    status
)
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from login import documentation as DOC
from login.serializers import LoginSerializer
from login.services import (
    LoginService,
    LogoutService
)


class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    @swagger_auto_schema(**DOC.post_login)
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        params = serializer.validated_data
        token = LoginService.login(params['user'], params['password'])
        return Response(token, status=status.HTTP_201_CREATED)


class LogoutView(APIView):

    @swagger_auto_schema(**DOC.get_logout)
    def get(self, request):
        LogoutService.logout(request.user)
        return Response(status=status.HTTP_204_NO_CONTENT)
