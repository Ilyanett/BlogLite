from rest_framework.viewsets import ModelViewSet

from webapp.models import SubPost
from webapp.pagination import CustomPageNumberPagination
from webapp.serializers import SubPostSerializer


class PostViewSet(ModelViewSet):
    queryset = SubPost.objects.all()
    serializer_class = SubPostSerializer
    pagination_class = CustomPageNumberPagination