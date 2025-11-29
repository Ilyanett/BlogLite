from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from webapp.models import SubPost

from webapp.serializers import SubPostSerializer


class SubPostViewSet(ModelViewSet):
    queryset = SubPost.objects.all()
    serializer_class = SubPostSerializer
    pagination_class = PageNumberPagination