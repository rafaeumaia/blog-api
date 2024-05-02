from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Author')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='publish_date')
    body = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
