from django.urls import path
from .views import SubirImagenView, HealthCheckView

urlpatterns = [
    path('upload/', SubirImagenView.as_view()),
    path('upload/health/', HealthCheckView.as_view()),
]
