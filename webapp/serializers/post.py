from rest_framework.serializers import ModelSerializer
from webapp.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'author', 'created_at', 'updated_at', 'subposts']
        read_only_fields = ['id','created_at', 'updated_at', 'author']