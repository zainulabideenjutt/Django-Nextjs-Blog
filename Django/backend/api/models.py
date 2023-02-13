from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ConvertImage(models.Model):
    # Relationships
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    # Attributes
    to_file_type=models.CharField(max_length=10)
    image=models.ImageField(upload_to='uploads/',blank=True)
    converted=models.CharField(max_length=100,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
