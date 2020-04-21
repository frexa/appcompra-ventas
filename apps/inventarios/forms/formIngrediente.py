from django import forms
from apps.inventarios.models import Ingrediente
from datetime import datetime

class IngredienteForm(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields= ['receta','compra','nombre','precio_unit']
		labels={
		'receta':'Receta:',
		'compra':'Compra:',
		'nombre':'Nombre:',
		'precio_unit':'Precio:',
		}
		widgets={
		'receta':forms.TextInput(attrs={
	 							'class':'form-control',
	 							'placeholder':'Galletas'}),
		'compra':forms.Select(attrs={
									'class':'form-control',
									}),
		'nombre': forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'200000,00'
									}),
		'precio_unit':forms.TextInput(attrs={
								 	'class':'form-control',
								 	})
		}