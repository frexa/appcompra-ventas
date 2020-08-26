from django import forms
from apps.recetarios.models import*
class RecetaForm(forms.ModelForm):
	class Meta:
		model = Receta
		fields=['nombre','descripcion']

		labels={
		'nombre':'Nombre:',
		'descripcion':'Preparación:'
		}

		widgets={
		'nombre':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'Galletas confitadas'
			}),
		'descripcion':forms.Textarea(attrs={
			'class':'form-control',
			'placeholder':'Describa metodo de preparación (Opcional)',
			'required':'off'
			})
		}

class ElaborarForm(forms.ModelForm):
	class Meta:
		model = Elaboracion
		
		fields = ['receta', 'ingrediente','medida']
		
		labels = {
		'receta':'Receta',
		'ingrediente':'Ingrediente',
		'medida':'Medida'
		}

		widgets = {
		'receta':forms.Select(attrs={'class':'form-control'}),
		'ingrediente':forms.Select(attrs={'class':'form-control'}),
		'medida':forms.TextInput(attrs = {'class':'form-control'})
		}
		