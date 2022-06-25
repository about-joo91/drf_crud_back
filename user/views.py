import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

from .serializers import UserSerializer
# Create your views here.

class UserCreateView(APIView):
    def get(self,request):
        user = request.user
        return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
    def post(self, request):
        user_serializer = UserSerializer(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status= status.HTTP_400_BAD_REQUEST)
class UserControlView(APIView):
    def post(self, request):
        cur_user = authenticate(request, **request.data)
        if cur_user:
            login(request, cur_user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)