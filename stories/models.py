from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Story(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField() # full story
    preview_content = models.CharField(max_length=200, default='story preview...') # short story content
    slug = models.SlugField(max_length=120, unique=True, blank=True, default=slugify(title))
     
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)    
        super().save(*args, **kwargs)

    cover_picture = models.ImageField(
        upload_to='stories/covers/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    likes = models.ManyToManyField(User, related_name='liked_stories', blank=True)

    def __str__(self):
        return self.title
    
    def like(self, user):
        self.likes.add(user)

    def unlike(self, user):
        self.likes.remove(user)

    def is_liked_by_user(self, user):
        return self.likes.filter(id=user.id).exists()

    class Meta:
        db_table = 'Story'
        ordering = ['-created_at']


class Comment(models.Model):
    story = models.ForeignKey(Story, related_name='comments', on_delete=models.CASCADE, null=False)
    comment_section = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return '%s - %s' % (self.story.title, self.author)
    
   

    class Meta:
        db_table = 'Comments'
        ordering = ['-created_at']
