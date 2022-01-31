from django.shortcuts import render
import requests

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializers
from .models import Post

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data)
