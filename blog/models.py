from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = RichTextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    Date  = models.DateField(default=timezone.now)
    

    like = models.ManyToManyField(User,related_name='Blog_likes',blank=True)
    

    def total_likes(self):
        return self.like.count()


    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user} commented on {self.post}"








        

