from django.db import models

class Orden(models.Model):
    cliente = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En Proceso'),
        ('finalizada', 'finalizada'),
    ], default='pendiente')

    def __str__(self):
        return f"Orden {self.id}"
    
class Tarea(models.Model):
    orden = models.ForeignKey(Orden, related_name='tareas', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    responsable = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    completada = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion