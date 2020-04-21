from django import forms
from apps.recetarios.models import Receta

class RecetaForm(forms.ModelForm):
	class Meta:
		model = Receta
		fields=['nombre', 'preparacion']

		labels={
		'nombre':'Nombre:',
		'preparacion':'Preparación:'
		}

		widgets={
		'nombre':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Galletas confitadas'
			}),
		'preparacion':forms.Textarea(attrs={
			'class':'form-control',
			'placeholder':'Describa metodo de preparación (Opcional)',
			'required':'off'
			})
		}