from django.urls import path
from apps.ventas import  views

urlpatterns=[
	path('registrar/ventas', views.Registrar.as_view(), name='registrar-ventas'),
	]