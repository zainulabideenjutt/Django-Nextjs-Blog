
# Create your api views here.
from rest_framework import status
from PIL import Image
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ConvertImage
from .serializers import ConvertImageSerializer
from rest_framework import generics
@api_view(['GET'])
def api_home(request, *args, **kwargs):
    body=request.body
    print(body)
    return Response({"message": "Hi there, this is your Django API response!!"})

class ConvertImageDetailAPIView(generics.RetrieveAPIView):
    queryset = ConvertImage.objects.all()
    serializer_class = ConvertImageSerializer

    # lookup_field = 'pk' ??
convert_image_detail_view = ConvertImageDetailAPIView.as_view()


class ConvertImageListCreateAPIView(generics.ListCreateAPIView):
    queryset = ConvertImage.objects.all()
    serializer_class = ConvertImageSerializer
    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    # def perform_create(self, serializer):
    #     image=str(serializer.validated_data.get('image').name)
    #     to_file_type=serializer.validated_data.get('to_file_type')
    #     splitted_image=image.split('.')
    #     file_name=splitted_image[0]
    #     converted_file=f'{file_name}.{to_file_type}'
    #     serializer.save(converted=converted_file)


convert_image_list_create_view = ConvertImageListCreateAPIView.as_view()


class ConvertImageDeleteAPIView(generics.DestroyAPIView):
    queryset = ConvertImage.objects.all()
    serializer_class = ConvertImageSerializer


convert_image_delete_view = ConvertImageDeleteAPIView.as_view()