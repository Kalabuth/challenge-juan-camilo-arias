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
    

   
class ListarTareas(generics.ListAPIView):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]

class CrearTareas(generics.CreateAPIView):
    serializer_class = TareasSerializers
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    
class EliminarTareas(generics.DestroyAPIView):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    
class ActualizarTarea(generics.UpdateAPIView):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    renderer_classes = [ResponseRender]
    permission_classes = [IsAuthenticated]
    
class FiltrarTareaByFechaLimite(generics.ListAPIView):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get (self,request):
        fecha_limite = request.query_params.get('fecha_limite')
        fecha_limite_format = datetime.strptime(fecha_limite,'%Y-%m-%d').date()
        
        tareas = Tareas.objects.filter(fecha_limite = fecha_limite_format)
        
        if tareas: 
            serializador = self.serializer_class(tareas,many=True)
            return Response({'success':True,'detail':'Se encontraron tareas','data':serializador.data},status=status.HTTP_200_OK)
    
        return Response({'success':True,'detail':'No se encontraron tareas'},status=status.HTTP_200_OK)
    
class FiltrarTareasByPersona(generics.ListAPIView):
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        nro_documento = request.query_params.get('nro_documento')
        tipo_documento = request.query_params.get ('tipo_documento')
        
        tareas = self.queryset.all().filter(persona__numero_documento = nro_documento, persona__tipo_documento = tipo_documento )
        
        if tareas:
            serializador = self.serializer_class(tareas,many = True)
            
            return Response({'success':True,'detail':'Se encontraron tareas','data':serializador.data},status=status.HTTP_200_OK)
            
        return Response({'success':True,'detail':'No se encontraron tareas'},status=status.HTTP_200_OK)


class CrearUsuario(generics.CreateAPIView):
    serializer_class = UsuarioSerializers
    queryset = User.objects.all()
    renderer_classes = [ResponseRender]
    

class LoginViews(TokenObtainPairView):
    renderer_classes = [ResponseRender]
    

class FiltrarTareasByRangoFecha(generics.ListAPIView):
    
    serializer_class = TareasSerializers
    queryset = Tareas.objects.all()
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        
        desde = request.query_params.get('desde')
        hasta = request.query_params.get('hasta')
        
        fecha_desde_format = datetime.strptime(desde,'%Y-%m-%d').date()
        fecha_hasta_format = datetime.strptime(hasta,'%Y-%m-%d').date()
        
        tareas = self.queryset.all().filter(fecha_limite__gte=fecha_desde_format, fecha_limite__lte = fecha_hasta_format)
        
        if tareas:
            serializador = self.serializer_class(tareas,many=True)
            return Response({'success':True,'detail':'Se encontraron tareas','data':serializador.data},status=status.HTTP_200_OK)
        
        return Response({'success':True,'detail':'No se encontraron tareas'},status=status.HTTP_200_OK)