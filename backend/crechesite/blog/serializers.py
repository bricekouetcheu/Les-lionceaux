from rest_framework import serializers
from blog.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    """
    Serializer for Blog model.
    """

    class Meta:
        model = Blog
        fields = "__all__"