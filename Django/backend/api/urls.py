from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
urlpatterns = [
    path('', views.api_home),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # Convert Image
    path('convertedimages',views.convert_image_list_create_view),
    path('convertedimages/<int:pk>',views.convert_image_detail_view),
    path('convertedimages/<int:pk>/delete',views.convert_image_delete_view),
]

