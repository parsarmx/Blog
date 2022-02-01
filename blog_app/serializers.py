from abc import ABC

from rest_framework import serializers

from blog_app.models import Post, Comment, Like


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user',
            'post',
            'created',
        )


class PostSerializers(serializers.ModelSerializer):
    likes = LikeSerializers(source='like_set', many=True)

    class Meta:
        model = Post
        fields = (
            'author_id',
            'title',
            'description',
            'photos',
            'date_and_time',
            'num_likes',
            'likes'
        )
