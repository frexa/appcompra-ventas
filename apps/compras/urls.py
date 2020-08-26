from django.urls import path, include
from apps.compras.views import*

urlpatterns=[
	path('',index, name = 'index_co'),
	path('registrar/', include([
		path('fecha',RegistrarFecha.as_view(), name='registrar-fecha'),
		path('ingrediente',RegistrarIngrediente.as_view(),name='registrar-ingrediente'),
		path('compra',RegistrarLineaCompra.as_view(),name='registrar-compra')])),
	path('actualizar/',include([
		path('<int:pk>/fecha',ActualizarFecha.as_view(),name = 'actualizar-fecha'),
		path('<uuid:pk>/compra',ActualizarLineaCompra.as_view(),name = 'actualizar-compra'),
		path('<uuid:pk>/ingrediente',ActualizarIngrediente.as_view(),name = 'actualizar-ingrediente')])),
	path('eliminar/',include([
		path('<int:pk>/fecha',EliminarFecha.as_view(),name = 'eliminar-fecha'),
		path('<int:pk>/compra',EliminarLineaCompra.as_view(),name = 'eliminar-compra'),
		path('<uuid:pk>/ingrediente',EliminarIngrediente.as_view(),name = 'eliminar-ingrediente')])),
	path('listar/',include([
		path('compras', ListarCompras.as_view(),name = 'listar-compras')])),
	path('detalles/',include([ 
		path('<uuid:pk>/compra',DetallesCompra.as_view(), name = 'detalles-compra')])),
	path('reporte', reporte_compras_semanales, name='compras-semanales')
	]