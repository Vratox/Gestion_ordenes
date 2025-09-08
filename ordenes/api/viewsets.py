from rest_framework.viewsets import ModelViewSet
from ..models import Orden
from .serializers import OrdenSerializer

class OrdenViewSet(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer