
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    path(
        'cadastro/',
        views.cadastrar_doacao,
        name='cadastrar_doacao'
    ),

    path(
        'historico/',
        views.historico,
        name='historico'
    ),
]