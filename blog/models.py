from pickle import TRUE
from django.db import models

# Create your models here.
# https://www.youtube.com/watch?v=m3hhLE1KR5Q
# creamos la base super admin 123 pa@g.co


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-date_added']
        #ordena por fecha a post

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)        
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['date_added'] 