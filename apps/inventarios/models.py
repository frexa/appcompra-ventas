from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone

# Create your models here.

class Producto(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código único para cada producto")
	receta = models.ForeignKey('Receta',null=True, on_delete=models.CASCADE)
	nombre = models.CharField(max_length= 20)
	cantidad = models.IntegerField(default=0)
	costo = models.FloatField(default=0.00)
	fecha_emicion = models.DateField( default = timezone.now,null=True, blank=True)

	def __str__(self):
		return '%s','%s'%(self.nombre, self.fecha_emicion)
	
	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.id)])



class Ingrediente(models.Model):
	nombre = models.CharField(max_length= 20)
	cantidad = models.IntegerField(default=0)
	precio = models.FloatField(default=0.00)
	fecha_compra = models.DateField(default = timezone.now)

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('ingrediente-detail', args=[str(self.id)])

class Receta(models.Model):
	ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE, null= True, blank=True)
	nombre = models.CharField(max_length=30)
	medida = models.FloatField(default=0.00)
	preparacion = models.TextField(null= True, blank= True)

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('receta-detail', args=[str(self.id)])

class Venta(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código único para cada venta")
	producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	total = models.FloatField(default=0.00)
	fecha_venta = models.DateField(default = timezone.now)

	def __str__(self):
		return '%s','%d','%f','%s' %(self.producto.nombre, self.cantidad, self.total,self.fecha_venta)
	
	def get_absolute_url(self):
		return reverse('venta-detail', args=[str(self.id)])