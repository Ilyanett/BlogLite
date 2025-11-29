from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from webapp.models import Post
from webapp.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = PageNumberPagination