from django.db.models import fields
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Post, Comment, Share, Like

class PostSerializer(ModelSerializer):
    share = IntegerField(source="get_num_share",read_only =True)
    likes = IntegerField(source="get_num_like",read_only = True)
    comment = IntegerField(source="get_num_comment",read_only=True)
    username = CharField(source="user.username",read_only=True)
    class Meta:
        model = Post
        fields =["text", "likes","share","created_on","comment","username", "user"]

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = ["post", "user"]

class Shareserializer(ModelSerializer):
    class Meta:
        model = Share
        fields = ["post", "user"]
        # depth = 1


class Commentserializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ["post","user"]


