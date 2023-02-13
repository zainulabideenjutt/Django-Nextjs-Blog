from rest_framework.routers import DefaultRouter
from blogs.viewsets import PostViewSet

router=DefaultRouter()
router.register('posts',PostViewSet,basename='posts')
urlpatterns=router.urls