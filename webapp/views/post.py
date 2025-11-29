from rest_framework.viewsets import ModelViewSet

from webapp.models import Post
from webapp.pagination import CustomPageNumberPagination
from webapp.serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPageNumberPagination