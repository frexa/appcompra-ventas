from django.contrib import admin
from .models import Producto, Venta, Ingrediente, Receta
# Register your models here.

admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Ingrediente)
admin.site.register(Receta)