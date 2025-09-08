# ordenes/repositories/orden_repository.py
from ordenes.models import Orden

class OrdenRepository:
    @staticmethod
    def create(orden):
        orden.save()
        return orden
    
    @staticmethod
    def get_by_id(orden_id):
        return Orden.objects.filter(id=orden_id).first()
    
    @staticmethod
    def list_all():
        return Orden.objects.all()
