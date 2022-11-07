from django.urls import path

from .views import index, contato, pedido, produto

urlpatterns = [
    path('', index, name='index'),
    path('contato', contato, name='contato'),
    path('pedidos', pedido, name='pedidos'),
    path('produto<int:pk>', produto, name='produto'),
]
