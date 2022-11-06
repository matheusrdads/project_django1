from django.urls import path

from .views import index, contato, pedido

urlpatterns = [
    path('', index),
    path('contato', contato),
    path('pedidos', pedido)
]
