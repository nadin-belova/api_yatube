from posts.models import Post
from rest_framework import viewsets

from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet:
    pass


class GroupViewSet:
    pass

