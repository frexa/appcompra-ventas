from django.urls import path, include
from apps.recetarios.views import*

urlpatterns = [
path('registrar/', include([
		path('receta',RegistrarReceta.as_view(), name='registrar-receta'),
		path('formula',RegistroElaboracion.as_view(),name='registro-elaboracion')])),
path('actualizar/',include([
		path('<int:pk>/receta',ActualizarReceta.as_view(),name = 'actualizar-receta'),
		path('<int:pk>/formula',ActualizarFormula.as_view(),name = 'actualizar-formula')])),
path('eliminar/',include([
		path('<int:pk>/receta',EliminarRecetas.as_view(),name = 'eliminar-receta'),
		path('<int:pk>/formula',EliminarElaboracion.as_view(),name = 'eliminar-elaboracion')])),
path('listar/',include([
		path('recetas', ListarRecetas.as_view(),name='listar_receta')])),
path('detalles/',include([ 
		path('<int:pk>/receta',DetallesReceta.as_view(), name = 'detalles-receta')])),
	]