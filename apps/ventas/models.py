from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
from apps.inventarios.models import Producto
# Create your models here.

class Venta(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código único para cada venta")
	producto = models.ForeignKey(Producto, null=True, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	total = models.FloatField(default=0.00)
	fecha_venta = models.DateField(default = timezone.now)

	def __str__(self):
		return '%s'%(self.producto.nombre)
	
	def get_absolute_url(self):
		return reverse('venta-detail', args=[str(self.id)])