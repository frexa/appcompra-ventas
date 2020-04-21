from django.contrib import admin
from apps.inventarios.models import Producto,Ingrediente
from apps.ventas.models import Venta
from apps.compras.models import Compra
from apps.recetarios.models import Receta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Ingrediente)
admin.site.register(Receta)