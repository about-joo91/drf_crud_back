from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer


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