# ordenes/services/orden_service.py
from ordenes.repository.orden_repository import OrdenRepository
from ordenes.services.servicios import crear_tarea


class OrdenService:
    @staticmethod
    def crear_orden(form, usuario):
        orden = form.save(commit=False)
        orden.cliente = usuario
        orden.estado = 'pendiente'
        
        # Guardar en BD usando repositorio
        orden = OrdenRepository.create(orden)
        
        # Lógica adicional
        crear_tarea(orden, usuario)
        
        return orden
