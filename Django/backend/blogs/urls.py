from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns=[
    path('',views.post_api),
    path('posts',views.post_list_create_view),
    path('posts/<int:pk>',views.post_detail_view),
    path('posts/<int:pk>/update',views.post_update_view),
    path('posts/<int:pk>/delete',views.post_delete_view),
    # categories
    path('categories',views.post_category_list_create_view),
    path('categories/<int:pk>',views.post_category_detail_view),
    path('categories/<int:pk>/update',views.post_category_update_view),
    path('categories/<int:pk>/delete',views.post_category_delete_view),
    # Comment
    path('comments',views.post_comment_list_create_view),
    path('comments/<int:pk>',views.post_comment_detail_view),
    path('comments/<int:pk>/update',views.post_comment_update_view),
    path('comments/<int:pk>/delete',views.post_comment_delete_view),
    # User
    path('users',views.user_detail_view),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)