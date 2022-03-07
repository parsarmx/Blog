from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializers
from .models import Post, SubCategory
from users_app.models import Profile

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class MainAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()

        serializers = PostSerializers(posts, many=True)

        return Response(serializers.data)


class AddPostAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    # def get(self, request):
    #     return Response(data={'message': 'Add Post Section'})

    def post(self, request):
        user = Profile.objects.get(username=request.user.username)
        category = SubCategory.objects.get(name=request.data['category'])
        Post.objects.create(
            author=user,
            category=category,
            title=request.data['title'],
            description=request.data['description'],
            photos=request.data['photos']
        ).save()

        return Response(data={'message': 'Post Created'})


class UpdatePostAPIView(APIView):
    def get(self, request):
        return Response(data={'message': 'Update Post Section'})

    def post(self, request):
        pass


class ViewPostAPIView(APIView):

    def get(self, request, category, post_id):
        post = Post.objects.get(category__name=category, id=post_id)
        serializer = PostSerializers(post)
        return Response(serializer.data)
