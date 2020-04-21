from django import forms
from apps.inventarios.models import Receta

class RecetaForm(forms.ModelForm):
	class Meta:
		model = Receta
		fields=['ingrediente', 'nombre', 'medida', 'preparacion']

		labels={
		'ingrediente':'Ingrediente:',
		'nombre':'Nombre:',
		'medida':'Porcion:',
		'preparacion':'Preparación:'
		}

		widgets={
		'ingrediente':forms.Select(attrs={
			'class':'form-control',
			}),
		'nombre':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Galletas confitadas'
			}),
		'medida':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'200'
			}),
		'preparacion':forms.Textarea(attrs={
			'class':'form-control',
			'placeholder':'Describa metodo de preparación (Opcional)',
			'required':'off'
			})
		}