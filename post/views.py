from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import PostModel
from .serializer import PostSerializer


class PostView(APIView):
    def post(self, request):
        cur_user = request.user
        request.data['author'] = cur_user
        post_serializer = PostSerializer(data = request.data)
        if post_serializer.is_valid():
            post_serializer.save(author = cur_user)
            return Response(post_serializer.data, status= status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request):
        cur_user = request.user
        post_models = PostModel.objects.filter(author = cur_user)
        return Response(PostSerializer(post_models, many=True).data, status=status.HTTP_200_OK)
    def delete(self, request):
        post_id = request.query_params.get('post_id')
        post_obj = PostModel.objects.get(id = post_id)
        post_obj.delete()
        return Response({
            "message" : "성공적으로 삭제되었습니다."
        },status=status.HTTP_200_OK)
    def put(self, request):
        post_id = request.query_params.get('post_id')
        post_obj = PostModel.objects.get(id=post_id)
        post_serializer = PostSerializer(post_obj, data = request.data, partial=True)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status= status.HTTP_200_OK)
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)