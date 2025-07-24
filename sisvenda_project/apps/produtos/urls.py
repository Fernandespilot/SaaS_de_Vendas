from django.urls import path
from . import views

app_name = 'produtos'

urlpatterns = [
    path('', views.listar_produtos, name='listar_produtos'),
    path('<int:produto_id>/', views.detalhar_produto, name='detalhar_produto'),
    path('buscar/', views.buscar_produtos, name='buscar_produtos'),
    path('<int:produto_id>/info/', views.get_produto_info, name='get_produto_info'),
    path('lista/', views.listar_produtos, name='lista'),
]
