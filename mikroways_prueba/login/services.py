from typing import Dict
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers


class LoginService:
    '''
    Servicio que realiza el login de un user. Dado un user y password si los
    mismos son correctos se retorna un token para el usuario.
    '''

    @classmethod
    def login(cls, user: str, password: str) -> Dict:
        user = authenticate(username=user, password=password)
        if not user:
            raise serializers.ValidationError('Credenciales inválidas.')
        token = Token.objects.get_or_create(user=user)[0]
        return {'token': token.key}


class LogoutService:
    '''
    Servicio que deslogea al user. Elimina el token rest.
    '''

    @classmethod
    def logout(cls, user: User) -> None:
        user.auth_token.delete()
