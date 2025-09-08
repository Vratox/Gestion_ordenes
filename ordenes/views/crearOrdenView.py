from django.shortcuts import render, redirect
from django.views import View 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseBadRequest
from ..forms import Orden_forms
from ordenes.services import crear_tarea
import json

from cliente.models import Cliente

@method_decorator(login_required, name='dispatch')
class ordenes_view(View):    
    def get(self, request):    
        forms = Orden_forms()    
        return render(request, 'orden.html', {'forms': forms})
    
    def post(self, request):    
        try:
            data = json.loads(request.body)     
            form = Orden_forms(data)           

            usuario = request.user
            # cliente = Cliente.objects.filter(id= 1 ).first()
            
            if form.is_valid():
                print("Formulario es valido")
                orden = form.save(commit=False)
                
                
                # orden.titulo = data.get('titulo')
                # orden.descripcion = data.get('descripcion')
                orden.cliente = usuario
                orden.estado = 'pendiente'
                
                orden.save()    
                
                crear_tarea(orden,usuario)   
                         
                return  JsonResponse({'success': True, 'message': 'Orden guardado con exito'})      
            else: 
                return JsonResponse(form.errors, status = 400)
        except Exception as e:
            return JsonResponse({'mesagge': str(e)}, status = 500)

         
            