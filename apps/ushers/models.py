from django.db import models

# Create your models here.
class Usuario (models.Model):
	nombre = models.CharField(max_length=20)
	password = models.CharField(max_length=30, unique=True)
	def __str__(self):
		return '%s', '%s' %(self.nombre, self.password)