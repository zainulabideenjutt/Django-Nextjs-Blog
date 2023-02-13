from rest_framework import serializers

from . models import ConvertImage


class ConvertImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConvertImage
        fields = [
            'id',
            'author',
            'image',
            'to_file_type',
            'converted'
        ]