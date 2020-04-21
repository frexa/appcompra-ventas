from django import forms
from apps.inventarios.models import Ingrediente
from datetime import datetime

class IngredienteForm(forms.ModelForm):
	class Meta:
		model = Ingrediente
		fields= ['receta','compra','nombre','medida']
		labels={
		'receta':'Receta:',
		'compra':'Compra',
		'nombre':'Nombre:',
		'medida':'Medida:',
		}
		widgets={
		'receta':forms.TextInput(attrs={
	 							'class':'form-control',
	 							'placeholder':'Galletas'}),
		'compra':forms.SelectDateWidget(attrs={
									'class':'form-control',
									}),
		'nombre': forms.TextInput(attrs={
									'class':'form-control',
									'placeholder':'200000,00'
									}),
		'medida':forms.SelectDateWidget(attrs={
								 	'class':'form-control',
								 	'placeholder':'12/04/2020'
								 	})
		}