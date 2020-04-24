from django.urls import path, include
from apps.compras.views import*

urlpatterns=[
	path('',index, name = 'index'),
	path('registrar/', include([
		path('compra',RegistrarCompra.as_view(), name='registrar-compra'),
		path('ingrediente',RegistrarIngrediente.as_view(),name='registrar-ingrediente'),
		path('linea',RegistrarLineaCompra.as_view(),name='registrar-linea')])),
	path('actualizar/',include([
		path('<int:pk>/compra',ActualizarCompra.as_view(),name = 'actualizar-compra'),
		path('<int:pk>/linea',ActualizarLineaCompra.as_view(),name = 'actualizar-linea'),
		path('<int:pk>/ingrediente',ActualizarIngrediente.as_view(),name = 'actualizar-ingrediente')])),
	path('eliminar/',include([
		path('<int:pk>/compra',EliminarCompra.as_view(),name = 'eliminar-compra'),
		path('<int:pk>/linea',EliminarLineaCompra.as_view(),name = 'eliminar-linea'),
		path('<int:pk>/ingrediente',EliminarIngrediente.as_view(),name = 'eliminar-ingrediente')])),
	]