from django import forms
from apps.compras.models import*

class FechaDeCompraForm(forms.ModelForm):
	class Meta:
		model = FechaDeCompra
		
		fields = ['id','fecha']

		labels={'id':'Código','fecha':'Fecha de compra:'}

		widgets={
		'id':forms.TextInput(attrs={'class':'form-control'}),
		'fecha':forms.SelectDateWidget(attrs={'class':'form-control'})
		}

class LineaDeCompraForm(forms.ModelForm):
	class Meta:
		model = LineaDeCompra

		fields= ['id','fecha', 'ingrediente', 'cantidad','total']
		
		lebels={'fecha':'Fecha de compra:','ingrediente':'Rubro:',
		'cantidad':'Cantidad:',
		'total':'Total a pagar:',
		'id':'Código'
		}
		
		widgets={
		'fecha':forms.Select(attrs={'class':'form-control'}),
		'ingrediente':forms.Select(attrs={'class':'form-control'}),
		'cantidad':forms.TextInput(attrs={'class':'form-control'}),
		'total':forms.TextInput(attrs={'class':'form-control'}),
		'id':forms.TextInput(attrs={'class':'form-control'})
		}

class IngredienteForm(forms.ModelForm):
	class Meta:
		model = Ingrediente

		fields=['id','nombre','peso','precio_unit','status']
		
		lebels={
		'id':'Código de ingrediente:','nombre':'Nombre:','peso':'Peso:',
		'precio_unit':'Precio:','status':'Estado del ingrediente:'
		}
		
		widgets={
		'id':forms.TextInput(attrs={'class':'form-control'}),
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'peso':forms.TextInput(attrs={'class':'form-control'}),
		'precio_unit':forms.TextInput(attrs={'class':'form-control'}),
		'status':forms.TextInput(attrs={'class':'form-control'})
		}