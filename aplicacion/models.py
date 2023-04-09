from django.db import models
from aplicacion.choices import tipo_documento_CHOICES,sexo_CHOICES
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Personas(models.Model):
    id_persona = models.AutoField(primary_key=True,editable=False)
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30,blank=True,null=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30,blank=True,null=True)
    tipo_documento = models.CharField(max_length=2,choices=tipo_documento_CHOICES)
    numero_documento = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=True,null=True)
    sexo = models.CharField(max_length=1, null=True, blank=True, choices=sexo_CHOICES)
    edad = models.PositiveIntegerField()
    
    def __str__(self):
        return str(self.id_persona)
    
    class Meta:
        unique_together = ['numero_documento','tipo_documento']
    
    
class Tareas(models.Model):
    id_tarea = models.AutoField(primary_key=True,editable=False)
    titulo = models.CharField(max_length=150,unique=True)
    descripcion = models.TextField()
    fecha_limite = models.DateField()
    persona = models.ForeignKey(Personas,on_delete=models.SET_NULL,blank=True,null =True)
    
    def __str__(self):
        return str(self.id_tarea)
    
class User(AbstractUser):
    email = models.EmailField("email address",unique=True)
    
    USERNAME_FIELD="email"
    
    REQUIRED_FIELDS=["username"]
    
    
    
    
    
    
    
    
    