from django.urls import path, include
from .import views

urlpatterns = [
    
   
    path('', views.pacientes, name="pacientes"),
    #path('<int:id', views.paciente_view, name="pacientes.view"),
    #path('<atualizar:id', views.atualizar_view, name="atualizar.view"),
] 