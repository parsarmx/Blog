from django.db import models
from users_app.models import Profile
from tinymce import models as tinymce_models


class Post(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = tinymce_models.HTMLField()
    photos = models.ImageField(default=None)
    date_and_time = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = tinymce_models.HTMLField()


class Like(models.Model):
    pass
