from django.contrib import admin
from apps.compras.models import Compra, LineaDeCompra, Ingrediente

# Register your models here.

admin.site.register(Compra)
admin.site.register(LineaDeCompra)
admin.site.register(Ingrediente)