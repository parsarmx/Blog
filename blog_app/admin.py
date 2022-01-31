from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'photos', 'description']


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ['blog_post', 'author', 'description']
