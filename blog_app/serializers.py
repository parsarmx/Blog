from abc import ABC

from rest_framework import serializers

from blog_app.models import Post, Comment, Like


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'blog_post',
            'author',
            'description',
            'created,'
        )


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = (
            'user',
            'post',
            'created',
        )


class PostSerializers(serializers.ModelSerializer):
    # likes = LikeSerializers(source='like_set', many=True)

    class Meta:
        model = Post
        fields = (
            'author',
            'title',
            'description',
            'photos',
            'date_and_time',
            'num_likes',
            'get_absolute_url',
            # 'likes'
        )
