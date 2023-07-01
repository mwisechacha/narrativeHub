from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    cover_picture = models.ImageField(
        upload_to='stories/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Story'
        ordering = ['-created_at']


class Comment(models.Model):
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    story = models.ForeignKey(Story, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.author

    class Meta:
        db_table = 'Comments'
        ordering = ['-created_at']
