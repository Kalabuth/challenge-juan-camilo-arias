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

]
