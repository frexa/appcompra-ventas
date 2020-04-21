from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
# Create your models here.

class Compra(models.Model):
	"""docstring for Compras"""
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Código unico para cada compra")
	cantidad = models.IntegerField(default=0 ,blank=True,null=True)
	peso = models.FloatField(default=0.00, blank=True,null=True)
	precio_unt = models.FloatField(default  = 0.00)
	total = models.DoubleField(default  = 0.00)
	fecha_compra = models.DateField(default = timezone.now, blank=True, null=True)

	def __str__(self):
		return '%s'%(self.fecha_compra)

	def get_absolute_url(self):
		return reverse('compra-detail', args=[srt(self.id)])