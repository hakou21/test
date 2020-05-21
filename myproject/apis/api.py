from apis.models import vicer
from rest_framework import viewsets, permissions
from .serializers import vicerserializer

class vicerviewset(viewsets.ModelViewSet):
    queryset=vicer.objects.all()
    permission_classes=[
        permissions.AllowAny
    ]
    serializer_class=vicerserializer