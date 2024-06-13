from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView
from home.models import Blog
from .serializers import BlogSerializer
from rest_framework.permissions import IsAuthenticated

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class BlogUpdateAPIView(UpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "pk"

class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated]
