from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from django.contrib.auth.hashers import make_password

from aplicacion.models import Personas, Tareas, User


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Personas
        
        validators = [
                UniqueTogetherValidator(
                    queryset=Personas.objects.all(),
                    fields = ['tipo_documento', 'numero_documento'],
                    message = 'Ya existe un registro con el tipo de documento y el número de documento ingresado'
                )
            ]
class TareasSerializers(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Tareas
        
class UsuarioSerializers(serializers.ModelSerializer):
    
    def validate_password(self, value) :
        return make_password(value)
    
    class Meta:
        fields = '__all__'
        model = User
