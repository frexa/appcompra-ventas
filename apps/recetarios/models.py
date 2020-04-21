from django.db import models
import uuid
from django.urls import reverse
from datetime import date
from django.utils import timezone
from apps.inventarios.models import Ingrediente
# Create your models here.

class Receta(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField(null= True, blank= True, help_text="Esta descripcion es opcional")

	def __str__(self):
		return '%s'%(self.nombre)
	
	def get_absolute_url(self):
		return reverse('receta-detail', args=[str(self.id)])