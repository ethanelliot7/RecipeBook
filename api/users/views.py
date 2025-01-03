from django.contrib.auth.models import User
from rest_framework import status
from api.users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


    def get_user(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        user = self.get_user(pk)
        serializer= UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self, request, pk):
        snippet = self.get_user(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        snippet = self.get_user(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
