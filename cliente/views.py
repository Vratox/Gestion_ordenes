from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from cliente.forms import Cliente_forms
from cliente.models import Cliente
from cliente.serializer import ClienteSerializer
import json

@method_decorator(login_required,name='dispatch')
class Cliente_view(View):
    
    def get(self, request):
        form = Cliente_forms()
        return render(request, 'cliente.html', {'form': form})
    
    def post(self, request):
        try:            
            data = json.loads(request.body)     
            form = Cliente_forms(data)
            if form.is_valid():
                form.save()
                
                User.objects.create_user(
                    username = data.get('nombre'),
                    first_name = data.get('nombre'),
                    email = data.get('email')
                )
                
                return  JsonResponse({'success': True, 'message': 'Cliente guardado con exito'})      
            else: 
                return JsonResponse(form.errors, status = 400)
        except Exception as e:
            return JsonResponse({'mesagge': str(e)}, status = 500)
        
@method_decorator(login_required, name='dispatch')
class ClienteJsonView(View):
    """
    Vista para manejar solicitudes GET y devolver una lista paginada de clientes en formato JSON.
    """

    def get(self, request, **kwargs):
        """
        Retorna una lista de clientes en formato JSON con paginación y ordenamiento.
        """
        total_items = Cliente.objects.all().order_by("id")
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
        data = ClienteSerializer(roles_page.object_list, many=True)
        
        # Preparar respuesta
        response_data = {
            "page": roles_page.number,
            "last_page": paginator.num_pages,
            "total_items": paginator.count,
            "data": data.data
        }
        return JsonResponse(response_data, safe=False)