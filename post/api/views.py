from rest_framework import viewsets

from post.api.serializers import PostSerializer, CommentSerializer
from ..models import Post, Comment


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """

    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited.
    """

    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
