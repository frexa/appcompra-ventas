from django.urls import path
from apps.compras.views import*

urlpatterns=[
	path('registrar/compras', RegistrarCompra.as_view(), name='registrar-compras'),
	]