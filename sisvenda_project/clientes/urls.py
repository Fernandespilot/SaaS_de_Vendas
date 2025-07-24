from django.urls import path
from . import views

app_name = 'clientes'

urlpatterns = [
    path('', views.lista_clientes, name='lista'),
    path('novo/', views.novo_cliente, name='novo'),
    path('<int:cliente_id>/', views.ver_cliente, name='ver'),
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar'),
    path('<int:cliente_id>/excluir/', views.excluir_cliente, name='excluir'),
    path('api/buscar-cep/', views.buscar_cep, name='buscar_cep'),
]
