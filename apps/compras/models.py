from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
# Create your models here.

class FechaDeCompra(models.Model):
	"""docstring for Compras"""
	id = models.UUIDField( primary_key=True,default = uuid.uuid4)
	fecha = models.DateField(default = timezone.now)

	def __str__(self):
		return '%s'%(self.fecha)

	def get_absolute_url(self):
		return reverse('detalles-compra', args=[str(self.id)])


class Ingrediente(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código único para cada ingrediente")
	nombre = models.CharField(max_length= 20)
	peso = models.FloatField(default = 0.0)
	precio_unit = models.FloatField()
	status = models.CharField(max_length = 20)

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('ingrediente-detail', args=[str(self.id)])

class LineaDeCompra(models.Model):
	"""docstring for LineaDeCompra"""
	fecha = models.ForeignKey(FechaDeCompra, on_delete = models.CASCADE)
	ingrediente = models.ForeignKey(Ingrediente, on_delete = models.CASCADE)
	cantidad = models.IntegerField(default=0)
	total = models.FloatField(default=0.0)

	def calculartotal(self, *args):
		self.total = self.cantidad * self.ingrediente.precio_unit
		return self.total

	def __str__(self):
		return '%s'%(self.fecha)

	def get_absolute_url(self):
		return reverse('detalles-compra', args=[str(self.id)])
