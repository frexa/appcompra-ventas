from django import forms
from apps.inventarios.models import Ingrediente
from datetime import datetime

class IngredienteForm(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields= ['nombre','cantidad','precio','fecha_compra']
		labels={
		'nombre':'Nombre:',
		'cantidad':'Cantidad:',
		'precio': 'Precio:',
		'fecha_compra':'Fecha de compra:'
		}
		widgets={
		'nombre':forms.TextInput(attrs={
	 							'class':'form-control',
	 							'placeholder':'Harina'}),
		'cantidad':forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'2'
									}),
		'precio': forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'200000,00'
									}),
		'fecha_compra':forms.SelectDateWidget(attrs={
								 	'class':'form-control',
								 	'placeholder':'12/04/2020'
								 	})
		}