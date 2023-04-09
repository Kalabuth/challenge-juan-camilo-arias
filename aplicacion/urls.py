from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from . import views

urlpatterns = [
    #Personas
    path('listar-personas/',views.ListPersonas.as_view(),name ='listar-personas'),
    path('crear-persona/',views.CreatePersona.as_view(),name ='Crear-personas'),
    path('actualizar-persona/<str:pk>/',views.ActualizarPersona.as_view(),name ='Actualizar-persona'),
    path('eliminar-persona/<str:pk>/',views.EliminarPersona.as_view(),name ='listar-personas'),
    path('filtrar-persona-by-documento/',views.FiltrarPersonaByDocumento.as_view(),name ='filtrar-persona-by-documento'),
    #Tareas
    path('listar-tareas/',views.ListarTareas.as_view(),name ='listar-tareas'),
    path('crear-tareas/',views.CrearTareas.as_view(),name ='crear-tareas'),
    path('actualizar-tarea/<str:pk>/',views.ActualizarTarea.as_view(),name ='actualizar-tareas'),
    path('eliminar-tarea/<str:pk>/',views.EliminarTareas.as_view(),name ='eliminar-tarea'),
    path('filtrar-tarea-by-fecha-limite/',views.FiltrarTareaByFechaLimite.as_view(),name ='filtrar-tarea-by-fecha-limite'),
    path('filtrar-tarea-by-persona/',views.FiltrarTareasByPersona.as_view(),name ='filtrar-tarea-by-persona'),
]
