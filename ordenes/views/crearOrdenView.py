# ordenes/views/ordenes_view.py
from django.shortcuts import render
from django.views import View 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

from ..forms import Orden_forms
from ordenes.services.orden_service import OrdenService


@method_decorator(login_required, name='dispatch')
class OrdenesView(View):    
    def get(self, request):    
        forms = Orden_forms()    
        return render(request, 'orden.html', {'forms': forms})
    
    def post(self, request):    
        try:
            data = json.loads(request.body)     
            form = Orden_forms(data)           
            usuario = request.user
            
            if form.is_valid():
                orden = OrdenService.crear_orden(form, usuario)
                return JsonResponse({'success': True, 'message': 'Orden guardada con éxito'})
            else: 
                return JsonResponse(form.errors, status=400)
                
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
