from rest_framework import serializers

from medusa.web.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['date', 'subject', 'content']
