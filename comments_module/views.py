from django.shortcuts import render
from rest_framework import generics
from .models import Users, Comments, Blog_posts
from .serializers import Users_serializer, comments_serializer, Blog_posts_serializer
# Create your views here.

class   Users_post_get(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = Users_serializer

class   Users_post_get_id(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = Users_serializer

class   Users_put(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = Users_serializer

class   Users_delete(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = Users_serializer