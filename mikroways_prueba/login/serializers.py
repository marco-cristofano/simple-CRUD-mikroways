from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    user = serializers.CharField()
    password = serializers.CharField()
