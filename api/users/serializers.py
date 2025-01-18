from django.contrib.auth.models import User
from rest_framework import serializers
from api.users.models import Profile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'username', 'email', 'profile_picture']
        extra_kwargs = {}


