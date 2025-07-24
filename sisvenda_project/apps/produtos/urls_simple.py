from django.urls import path
from . import views_simple

app_name = 'produtos'

urlpatterns = [
    path('', views_simple.lista_produtos, name='lista'),
    path('novo/', views_simple.novo_produto, name='novo'),
    path('<int:produto_id>/', views_simple.ver_produto, name='ver'),
    path('<int:produto_id>/editar/', views_simple.editar_produto, name='editar'),
    path('<int:produto_id>/excluir/', views_simple.excluir_produto, name='excluir'),
]
