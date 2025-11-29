from rest_framework.serializers import ModelSerializer
from webapp.models import SubPost

class SubPostSerializer(ModelSerializer):
    class Meta:
        model = SubPost
        fields = ['id', 'title', 'body', 'created_at', 'updated_at']
        read_only_fields = ['id','created_at', 'updated_at']