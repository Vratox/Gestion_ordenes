from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse
from ordenes.models import Orden
from ordenes.serializer import OrdenSerializer
import json


@method_decorator(login_required, name='dispatch')
class tableOrdenesJsonView(View):
    """
    Vista para manejar solicitudes GET y devolver una lista paginada de clientes en formato JSON.
    """

    def get(self, request, **kwargs):
        """
        Retorna una lista de clientes en formato JSON con paginación y ordenamiento.
        """
        total_items = Orden.objects.all().order_by("id")
        # Obtener parámetros de paginación
        page = int(request.GET.get("page", 1))
        size = int(request.GET.get("size", 10))

        sort_field = request.GET.get("sort[0][field]", "")
        sort_dir = request.GET.get("sort[0][dir]", "")

        if sort_field:
            if sort_dir == "desc":
                sort_field = f"-{sort_field}"
            total_items = total_items.order_by(sort_field)

        paginator = Paginator(total_items, size)
        roles_page = paginator.get_page(page)
        
        # Serializar los datos
        data = OrdenSerializer(roles_page.object_list, many=True)
        
        # Preparar respuesta
        response_data = {
            "page": roles_page.number,
            "last_page": paginator.num_pages,
            "total_items": paginator.count,
            "data": data.data
        }
        return JsonResponse(response_data, safe=False)