from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.vista, name='home'),
    path('genero/<str:categoria>/', views.ver_genero, name='ver_genero'),
]
