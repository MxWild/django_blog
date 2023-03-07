from rest_framework import generics, viewsets, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostSerializer
from blog.models import Post


@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all().order_by('-date_created')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


class PostList(APIView):
    # queryset = Post.objects.all().order_by('-date_created')
    # serializer_class = PostSerializer
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        posts = Post.objects.all().order_by('-date_created')
        return Response(posts)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
