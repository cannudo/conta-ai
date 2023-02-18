from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

from .serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)