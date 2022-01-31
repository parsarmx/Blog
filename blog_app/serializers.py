from rest_framework import serializers

from blog_app.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'author_id',
            'title',
            'description',
            'photos',
            'date_and_time',
        )
