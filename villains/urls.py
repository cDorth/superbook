# villains/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('lista/', VillainListView.as_view(), name='lista_viloes'),
    path('novo/', CreateVillain.as_view(), name='criar_vilao'),
    path('<int:pk>/editar/', UpdateVillain.as_view(), name='editar_vilao'),
    path('<int:pk>/deletar/', DeleteVillain.as_view(), name='excluir_vilao'),
]