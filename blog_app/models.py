from django.db import models
from users_app.models import Profile
from tinymce import models as tinymce_models
from django_jalali.db import models as jmodels


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=256)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Post(models.Model):
    category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = tinymce_models.HTMLField()
    photos = models.ImageField(default=None)
    date_and_time = jmodels.jDateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    def num_likes(self):
        return self.like_set.all().count()

    def get_absolute_url(self):
        return f'/post/{self.category}/{self.pk}'


class Comment(models.Model):
    blog_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = tinymce_models.HTMLField()
    created = jmodels.jDateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    created = jmodels.jDateTimeField(auto_now=True)
