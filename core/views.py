from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import json
 
class Login_views(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        try:                      
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)                
                return redirect('home')
            else:
                # return JsonResponse({'error': 'Nombre de usuario o contraseña incorrectos.'}, status=400)
                
                usuario = User.objects.filter(username=username).first()
                
                if usuario is not None:                                
                    if usuario.last_login == None:
                        print("El usuario nunca ha iniciado sesion")
                    
                        return render(request, 'login.html', {'user_new': " ", 'username': username})
                return render(request, 'login.html', {'error': "Nombre de usuario o contraseña incorrectos."})
                        
        except Exception as e:        
            return render(request, 'login.html', {'error': str(e)}, safe=False)
    
class Logout_view(View):
    def get(self, request):
        logout(request)
        return redirect( 'login_user')
    
@method_decorator(login_required, name='dispatch')    
class Home_view(View):
    def get(self, request):
        return render(request, 'home.html')
    
class RepeatPasswordView(View):
    def post(self, request):
        try:
            
            data = json.loads(request.body) 
            
            username = data.get('username')
            new_password = data.get('password')
            
            user = User.objects.filter(username=username).first()
            print(user)
            if user is not None:
                print("Usuario encontrado, actualizando contraseña")
                user.set_password(new_password)
                user.save()
                return JsonResponse({
                    "success": True,
                    "message": "Contraseña actualizada con éxito, por favor inicie sesión."
                }, status=200)
            else:
                return JsonResponse({
                    "success": False,
                    "error": "Usuario no encontrado."
                }, status=400)

        except Exception as e:
            return JsonResponse({
                "success": False,
                "error": str(e)
            }, status=500)