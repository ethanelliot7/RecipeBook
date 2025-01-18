from api.users.models import Profile
from rest_framework import generics
from .serializers import AuthSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny


class CreateUserView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = AuthSerializer
    permission_classes = [AllowAny]


