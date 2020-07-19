from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 54)
    text = models.TextField()
    create_date = models.DateTimeField(default = timezone.now())
    publish_date = models.DateTimeField(blank=True, null = True)

    def __str__(self):
        self.title

    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comment(self):
        self.comments.filter(approved_comment = True)

    def get_absolute_   url(self):
        return reverse('post_detail', kwargs = {'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name = 'comments')
    author = models.CharField(max_length = 51)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default = False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail')
