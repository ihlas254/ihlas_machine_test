from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class User(User):
    mobile = models.CharField(max_length=20, unique=True)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tags = models.CharField(max_length=100)
    save_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    likes = models.ManyToManyField(User, related_name='post_likes')


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')
