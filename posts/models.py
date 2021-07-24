from enum import auto
# from posts.serializers import Shareserializer
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Post(models.Model):
    text=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    def get_num_like(self):
        return Like.objects.filter(post=self).count()
    
    def get_num_share(self):
        return Share.objects.filter(post=self).count()

    def get_num_comment(self):
        return Comment.objects.filter(post=self).count()
    
class Like(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and post pair dont occure more thand once
        #e.g(user1, post1) can only exit once 
        unique_together = ("user","post")
    

class Share(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and post pair dont occure more thand once
        #e.g(user1, post1) can only exit once 
        unique_together = ("user","post",)


class Comment(models.Model):
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        #this makes sure that the user and post pair dont occure more thand once
        #e.g(user1, post1) can only exit once 
        unique_together = ("user","post")

