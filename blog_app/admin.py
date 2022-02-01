from django.contrib import admin
from .models import Post, Comment, Like


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'photos', 'description', 'date_and_time', 'num_likes']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['blog_post', 'author', 'description', 'created']


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['user', 'post', 'created']
