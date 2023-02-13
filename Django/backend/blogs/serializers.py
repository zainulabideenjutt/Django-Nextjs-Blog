from rest_framework import serializers
from django.contrib.auth.models import User
from . models import Post, PostCategory, PostComment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # [
        #     'id',
        #     'username'
        # ]
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'author',
            'featured_image',
            'title',
            'description',
            'summary',
            'views_count',
            'category',
        ]

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = [
            'id',
            'post',
            'author',
            'description',
        ]

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = [
            'id',
            'author',
            'name',
            'description',
            'parent',
            'child',
        ]