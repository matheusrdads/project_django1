from django.contrib import admin

from .models import Produto, Cliente, Pedidos


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')

class QuantidadeAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'quantidade')

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Pedidos, QuantidadeAdmin)
