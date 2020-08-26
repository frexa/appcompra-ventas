from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
from apps.compras.models import Ingrediente
# Create your models here.

class Receta(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(null= True, blank= True, help_text="Esta descripcion es opcional")

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('datalles-receta', args=[str(self.id)])

class Elaboracion(models.Model):
	"""docstring for Elaboracion"""
	receta = models.ForeignKey(Receta, on_delete = models.CASCADE)
	ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
	medida = models.FloatField(default=0.0)

	def __str__(self):
		return '%s' %(self.receta)
	
	def get_absolute_url(self):
		return reverse('datalles-receta', args=[str(self.id)])
	
	class Meta:
		verbose_name = "Elaboracion"