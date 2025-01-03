from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import AuthSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthSerializer
    permission_classes = [AllowAny]


