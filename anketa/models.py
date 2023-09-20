from django.db import models

# Create your models here.
# class Fotograf(models.Model):
#     title = models.CharField(max_length=255)
#     content = models.TextField(blank=True)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d')
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.title

from django.db import models
from django.utils.html import mark_safe


class Post(models.Model):
    title = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)

    @property
    def thumbnail_preview(self):
        if self.thumbnail:
            return mark_safe('<img src="{}" width="300" height="300" />'.format(self.thumbnail.url))
        return ""