from django.db import models

# Create your models here.

class Alumnos (models.Model): #Define la setructura de nuestra tabla
    matricula = models.CharField(max_length=12,verbose_name="Mat")#Texto corto
    nombre = models.TextField()#Texto largo
    carrera = models.TextField
    turno = models.CharField(max_length=10)
    imagen = models.ImageField(null=True,upload_to="fotos",verbose_name="Fotografía")
    created = models.DateTimeField(auto_now_add=True)#Fecha y Tiempo
    updated = models.DateTimeField(auto_now_add=True)

class Meta:
    verbose_name = "Alumno"
    verbose_name_plural = "Alumnos"
    ordering = ["-created"]
    #el menos indica que se ordenara del más reciente al mas viejo
def __str__(self):
    return self.nombre
    #Indica que se mostrára el nombre como valor en la tabla
