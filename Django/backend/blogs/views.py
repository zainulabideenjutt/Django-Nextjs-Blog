from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Post, PostCategory, PostComment
from rest_framework import generics,mixins,permissions,authentication
from .permissions import IsStaffEditor
from .mixins import StaffEditorPermissionsMixin
from blogs.serializers import PostSerializer, PostCommentSerializer, PostCategorySerializer,UserSerializer
from django.contrib.auth.models import User

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    return Response({"message": "Hi there, this is your Django API response From Blog!!"})


@api_view(['GET', 'POST'])
def post_api(request, *args, **kwargs):
    # print(dir(request))
    # print(request.GET['message']) 
    print(request.GET) #params
    print(request.body) #byte string json data
    # print(f"headers :{request.headers}")
    return HttpResponse("data",headers={'content-type':'application/json'})

class UserDetailAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

user_detail_view = UserDetailAPIView.as_view()

class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes=[permissions.IsAuthenticated]

    # lookup_field = 'pk' ??
post_detail_view = PostDetailAPIView.as_view()


class PostListCreateAPIView(
    # StaffEditorPermissionsMixin, # permission_classes=[permissions.IsAdminUser,IsStaffEditor]
    generics.ListCreateAPIView,
    ):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # authentication_classes=[authentication.SessionAuthentication]
    # permission_classes=[permissions.IsAdminUser,IsStaffEditor]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # print(dir(serializer))
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    


post_list_create_view = PostListCreateAPIView.as_view()


class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_update_view = PostUpdateAPIView.as_view()


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


post_delete_view = PostDeleteAPIView.as_view()


# Category
class PostCategoryDetailAPIView(generics.RetrieveAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

    # lookup_field = 'pk' ??
post_category_detail_view = PostCategoryDetailAPIView.as_view()


class PostCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


post_category_list_create_view = PostCategoryListCreateAPIView.as_view()


class PostCategoryUpdateAPIView(generics.UpdateAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


post_category_update_view = PostCategoryUpdateAPIView.as_view()


class PostCategoryDeleteAPIView(generics.DestroyAPIView):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer


post_category_delete_view = PostCategoryDeleteAPIView.as_view()

# Comment


class PostCommentDetailAPIView(generics.RetrieveAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    # lookup_field = 'pk' ??
post_comment_detail_view = PostCommentDetailAPIView.as_view()


class PostCommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


post_comment_list_create_view = PostCommentListCreateAPIView.as_view()


class PostCommentUpdateAPIView(generics.UpdateAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer


post_comment_update_view = PostCommentUpdateAPIView.as_view()


class PostCommentDeleteAPIView(generics.DestroyAPIView):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer


post_comment_delete_view = PostCommentDeleteAPIView.as_view()
