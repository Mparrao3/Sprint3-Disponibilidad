from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ImagenMedica
from .serializers import ImagenMedicaSerializer
from django.contrib.auth.models import User

class SubirImagenView(APIView):
    def post(self, request):
        usuario_id = request.data.get('usuario')
        if not User.objects.filter(id=usuario_id).exists():
            return Response({'error': 'Usuario no válido'}, status=400)
        
        # Simulación de carga (sin bucket aún)
        imagen = ImagenMedica.objects.create(
            nombre_archivo=request.data.get('nombre_archivo'),
            url_bucket='https://bucket-simulado/ruta.jpg',
            tipo_imagen=request.data.get('tipo_imagen'),
            usuario_id=usuario_id
        )
        return Response(ImagenMedicaSerializer(imagen).data, status=201)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({'status': 'ok'}, status=200)
