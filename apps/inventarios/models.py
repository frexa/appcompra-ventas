from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
from apps.inventarios.models import Receta,Compra

# Create your models here.

class Producto(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código único para cada producto")
	receta = models.ForeignKey('Receta', on_delete=models.CASCADE)
	nombre = models.CharField(max_length= 20)
	cantidad = models.IntegerField(default=0)
	costo = models.FloatField(default=0.00)
	fecha_emicion = models.DateField( default = timezone.now,null=True, blank=True)

	def __str__(self):
		return '%s','%s'%(self.nombre, self.fecha_emicion)
	
	def get_absolute_url(self):
		return reverse('producto-detail', args=[str(self.id)])



class Ingrediente(models.Model):
	compra = models.ForeignKey(Compra, on_delete = models.CASCADE)
	receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
	nombre = models.CharField(max_length= 20)
	modida = models.FloatField()

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('ingrediente-detail', args=[str(self.id)])