from django import forms
from apps.inventarios.models import Producto
from datetime import datetime

class ProductoForm(forms.ModelForm):
	class Meta:
		model = Producto
		fields= ['id','receta','nombre','cantidad','precio_unit','fecha_emicion']
		labels={
		'id':'Código:',
		'receta':'Receta:',
		'cantidad': 'Cantidad:',
		'precio_unit':'Precio',
		'fecha_emicion':'Fecha de emicion:'
		}
		widgets={
		'id':forms.TextInput(attrs={
	 							'class':'form-control',}),
		'receta':forms.Select(attrs={
									'class':'form-control',}),
		'nombre':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Galletas de chocolate'
			}),
		'catidad': forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'1'
									}),
		'fecha_emicion':forms.SelectDateWidget(attrs={
								 	'class':'form-control',
								 	'placeholder':'12/04/2020'
								 	}),
		'precio_unit':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'10000'
			})
		}