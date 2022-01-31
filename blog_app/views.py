from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializers
from .models import Post
from users_app.models import Profile

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class PostAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializers = PostSerializers(posts, many=True)
        return Response(serializers.data)


class AddPostAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = Profile.objects.get(username=request.user.username)
        Post.objects.create(
            author=user,
            title=request.data['title'],
            description=request.data['description'],
            photos=request.data['photos']
        ).save()

        return HttpResponse('success')
