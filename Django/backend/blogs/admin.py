from django.contrib import admin
from .models import Post
from .models import PostCategory
from .models import PostComment
# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(PostComment)
