from datetime import  datetime
from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from aplicacion.models import Personas, Tareas, User
from aplicacion.renderer import ResponseRender
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated


from aplicacion.serializadores import PersonaSerializer, TareasSerializers,UsuarioSerializers,LoginSerializer


class ListPersonas(generics.ListAPIView):
    serializer_class = PersonaSerializer
    queryset = Personas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    
class CreatePersona(generics.CreateAPIView):
    serializer_class = PersonaSerializer
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    

class EliminarPersona(generics.DestroyAPIView):
    serializer_class = PersonaSerializer
    queryset = Personas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    
class ActualizarPersona(generics.UpdateAPIView):
    serializer_class = PersonaSerializer
    queryset =  Personas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]

class FiltrarPersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer
    queryset = Personas.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        nro_documento = request.query_params.get('nro_documento')
        tipo_documento = request.query_params.get ('tipo_documento')
        
        personas = self.queryset.all().filter(tipo_documento = tipo_documento ,numero_documento = nro_documento).first()
        
        if personas:
            serializador = self.serializer_class(personas)
            return Response ({'success':True,'detail':'Busqueda exitosa, se encontró a la persona','data':serializador.data},status=status.HTTP_200_OK)
        
        return Response({'success':True,'detail':'No se encontro a la persona'},status=status.HTTP_200_OK)
    
