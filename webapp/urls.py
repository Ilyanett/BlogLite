from django.urls import path, include
from rest_framework import routers

from webapp.views import PostViewSet, SubPostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('subposts', SubPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
