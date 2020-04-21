from django.urls import path
from apps.inventarios.view import  viewsIngrediente, viewsProductos
from apps.inventarios import views

urlpatterns= [
	path('',views.index, name = 'index'),
	path('registrar/ingrediente', viewsIngrediente.Registrar.as_view(), name='registrar-ingrediente'),
	path('registrar/producto', viewsProductos.Registrar.as_view(), name='registrar-producto'),
	path('lista/ingredientes', viewsIngrediente.ListaIngrediente.as_view(), name = 'lista-ingredientes'),
	path('ingrediente/<int:pk>', viewsIngrediente.DetallesIngrediente.as_view(), name = 'ingrediente-detail'),
	path('ingrediente/<int:pk>/eliminar', viewsIngrediente.EliminarIngrediente.as_view(),name = 'ingrediente-eliminar'),
	path('ingrediente/<int:pk>/actualizar', viewsIngrediente.ActualizarIngrediente.as_view(),name= 'ingrediente-actualizar'),
	path('ingredientes', viewsIngrediente.InventarioIngredientes.as_view(), name='ingredientes'),
]