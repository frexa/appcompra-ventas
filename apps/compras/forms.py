from django import forms
from apps.compras.models import Compra, LineaDeCompra, Ingrediente

class CompraForm(forms.ModelForm):
	class Meta:
		model = Compra
		
		fields = ['id', 'fecha']

		labels={'id':'Código de compra:','fehca':'Fecha de compra:'}

		widgets={
		'id':forms.TextInput(attrs={'class':'form-control'}),
		'fecha':forms.SelectDateWidget(attrs={'class':'form-control'})
		}

class LineaDeCompraForm(forms.ModelForm):
	class Meta:
		model = LineaDeCompra

		fields= ['compra', 'ingrediente', 'cantidad','total']
		
		lebels={'compra':'Fecha de compra:','ingrediente':'Rubro:',
		'cantidad':'Cantidad:',
		'total':'Total a pagar:'
		}
		
		widgets={
		'compra':forms.Select(attrs={'class':'form-control'}),
		'ingrediente':forms.Select(attrs={'class':'form-control'}),
		'cantidad':forms.TextInput(attrs={'class':'form-control', 'type':'number'}),
		'total':forms.TextInput(attrs={'class':'form-control'})
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