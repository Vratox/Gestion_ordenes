from ordenes.models import Tarea  

array = ["Revision inicial", "Asignacion de responsable", "Confirmacion con cliente"]

def crear_tarea(orden,usuario):
    print(orden)
    print(usuario)
    for i in range(len(array)):
        Tarea.objects.create(            
            orden = orden,
            titulo = array[i],
            responsable = usuario                  
        )
    return 
    
# orden = models.ForeignKey(Orden, related_name='tareas', on_delete=models.CASCADE)
#     titulo = models.CharField(max_length=200)
#     reponsable = models.CharField(max_length=100)
#     completada = models.BooleanField(default=False)