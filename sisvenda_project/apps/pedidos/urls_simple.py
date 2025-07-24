from django.urls import path
from . import views_simple

app_name = 'pedidos'

urlpatterns = [
    path('', views_simple.lista_pedidos, name='lista'),
    path('novo/', views_simple.novo_pedido, name='novo'),
    path('<int:pedido_id>/', views_simple.ver_pedido, name='ver'),
    path('<int:pedido_id>/editar/', views_simple.editar_pedido, name='editar'),
    path('<int:pedido_id>/imprimir/', views_simple.imprimir_pedido, name='imprimir'),
]
