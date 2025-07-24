from django.contrib import admin
from .models import User, Cliente, PromotorVenda, Municipio


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'tipo_usuario', 'is_active']
    list_filter = ['tipo_usuario', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['user', 'municipio', 'promotor', 'limite_credito', 'status_financeiro']
    list_filter = ['status_financeiro', 'municipio', 'promotor']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']


@admin.register(PromotorVenda)
class PromotorVendaAdmin(admin.ModelAdmin):
    list_display = ['user', 'municipio', 'comissao', 'meta_mensal']
    list_filter = ['municipio', 'data_contratacao']
    search_fields = ['user__username', 'user__email', 'user__first_name', 'user__last_name']


@admin.register(Municipio)
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'estado']
    list_filter = ['estado']
    search_fields = ['nome']
