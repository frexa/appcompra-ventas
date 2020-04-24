from django.urls import path, include
from apps.compras.views import*

urlpatterns=[
	path('registrar/', include([
		path('compra',RegistrarCompra.as_view(), name='registrar-compra'),
		path('ingrediente',RegistrarIngrediente.as_view(),name='registrar-ingrediente'),
		path('linea',RegistrarLineaCompra.as_view(),name='registrar-linea')])),
	path('actualizar/',include([
		path('<int:pk>/compra',ActualizarCompra.as_view(),name = 'actualizar-compra'),
		path('<int:pk>/linea',ActualizarLineaCompra.as_view(),name = 'actualizar-linea'),
		path('<int:pk>/ingrediente',ActualizarIngrediente.as_view(),name = 'actualizar-ingrediente')])),
	]