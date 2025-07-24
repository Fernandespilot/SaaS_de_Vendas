from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_simple, name='dashboard'),
    path('simple/', views.dashboard_simple, name='simple'),
    path('test/', views.test_dashboard, name='test'),
]
