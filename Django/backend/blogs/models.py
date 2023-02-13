import os
from pathlib import Path
from datetime import date, datetime
from enum import unique
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # Attributes
    featured_image=models.ImageField('Uploaded Image',upload_to='uploads/',unique=False,blank=True)
    title=models.CharField(max_length=75,null=True,unique=False)
    description=models.TextField(null=True,unique=False)
    summary=models.CharField(max_length=50,unique=False)
    views_count=models.IntegerField(blank=True,unique=False,default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ManyToManyField('PostCategory',blank=True,unique=False)
    def __str__(self):
        return self.summary
    
    def image_tag(self):
        from django.utils.html import escape
        return u'<img src="%s" />' % escape(self.featured_image.url)
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
    
    # def save(self,*args,**kwargs):
    #     print(self.featured_image.name)
    #     date=datetime.now()
    #     print(date)
    #     os.rename(self.featured_image.name ,self.featured_image.name)
    #     super().save(*args, **kwargs)
        

class PostCategory(models.Model):
    # Relationships
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # attributes
    name=models.CharField(max_length=20)
    description=models.CharField(max_length=75,blank=True,null=True)
    parent=models.ManyToManyField('PostCategory',blank=True,related_name='category_parent')
    child=models.ManyToManyField('PostCategory',blank=True,related_name='category_child')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PostComment(models.Model):
    # Relationships
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    # attributes
    description=models.TextField(unique=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     if self.description:
    #         return self.description
    #     else:
    #         ''
        


