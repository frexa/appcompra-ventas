from django.urls import path
from apps.recetarios import views

urlpatterns = [
	path('registrar/receta', views.Registrar.as_view(), name='registrar-receta'),

]