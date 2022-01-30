from rest_framework.generics import ListAPIView

from medusa.web.models import Post
from .serializers import PostSerializer


class PostListAPIView(ListAPIView):
    """Список новостей"""

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.all().order_by('-date')
