from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import UserModel

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

class FollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, target_id):
        cur_user = request.user
        target_user = cur_user.follower.filter(id = target_id)
        if target_user.exists():
            cur_user.follower.remove(target_user.first())
            return Response({"message" : "팔로우 취소 되었습니다."})
        cur_user.follower.add(target_id)
        return Response({"message" : f"{target_user.first().nickname}님을 팔로우 했습니다."})
        