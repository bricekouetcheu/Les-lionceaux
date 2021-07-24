from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from blog.serializers import BlogSerializer
from blog.models import Blog


class BlogViewSet(viewsets.ModelViewSet):
    """
    Viewset for Blog model.
    """

    serializer_class = BlogSerializer
    queryset = Blog.objects.all()