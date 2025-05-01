from rest_framework import serializers
from .models import ImagenMedica

class ImagenMedicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenMedica
        fields = '__all__'
