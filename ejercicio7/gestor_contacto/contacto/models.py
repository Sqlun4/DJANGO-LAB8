from django.db import models

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length = 60)
    apellido =  models.CharField(max_length = 60)
    celular =  models.CharField(max_length = 10)
    email = models.EmailField()
    direccion = models.TextField(blank = True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
