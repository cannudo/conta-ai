from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    def create(self, dados):
        user = User.objects.create(
            username = dados['username'],
            email = dados['email'],
            first_name = dados['first_name'],
            last_name = dados['last_name']
        )
        user.set_password(dados['password'])
        user.save()

        return user