from django.urls import path, include

urlpatterns = [
    path('clientes_v1/', include("cliente.api.urls")),
    path('ordenes_v1/', include("ordenes.api.urls")),
]