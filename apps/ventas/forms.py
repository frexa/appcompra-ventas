from django import forms
from apps.ventas.models import Venta
from datetime import timezone

class VentasForm(forms.ModelForm):
	"""docstring for VentasForm"""
	class Meta:
		model = Venta
		fields = ['id', 'producto', 'cantidad', 'total', 'fecha_venta']
		
		labels = {
		'id':'Código:',
		'producto':'Producto:',
		'cantidad':'Cantidad:',
		'total':'Total a pagar:',
		'fecha_venta':'Fecha de venta'
		}

		widgets={
		'id': forms.TextInput(attrs={
			'class':'form-control'
			}),
		'producto':forms.Select(attrs={
			'class':'form-control',
			'placeholder':'Galletas',
			}),
		'cantidad':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'10'
			}),
		'total':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'250000'
			}),
		'fecha_venta':forms.Select(attrs={
			'class':'form-control'
			})
		}