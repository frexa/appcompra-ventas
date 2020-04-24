from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.compras.forms import*
from apps.compras.models import*

# Create your views here.
def index(request):
	ingrediente = Ingrediente.objects.all().count()
	numero_visitas = request.session.get('numero_visitas',0)
	request.session['numero_visitas'] = numero_visitas+1
	return render(request,'index.html', {'ingrediente':ingrediente,
										'numero_visitas':numero_visitas})
class RegistrarCompra(CreateView):
	"""docstring for RegistrarCompra"""
	model = Compra
	template_name = 'CrearCompra.html'
	form_class = CompraForm
	success_url = 'ingrediente'

	def get_context_data(self, **kwargs):
		context = super(RegistrarCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.model_form(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			compra = form.save(commit=False)
			compra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarCompra(UpdateView):
	"""docstring for ActualizarCompra"""
	model = Compra
	template_name = 'CrearCompra.html'
	form_class = CompraForm
	success_url = 'ingrediente'

	def get_context_data(self, **kwargs):
		context = super(RegistrarCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.model_form(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			compra = form.save(commit=False)
			compra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class RegistrarLineaCompra(CreateView):
	"""docstring for RegistrarCompra"""
	model = LineaDeCompra
	template_name = 'CrearLineaDeCompra.html'
	form_class = LineaDeCompraForm
	success_url = 'compra'

	def get_context_data(self, **kwargs):
		context = super(RegistrarLineaCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			lineacompra = form.save(commit=False)
			lineacompra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarLineaCompra(UpdateView):
	"""docstring for ActualizarLineaCompra"""
	model = LineaDeCompra
	template_name = 'CrearLineaDeCompra.html'
	form_class = LineaDeCompraForm
	success_url = 'compra'

	def get_context_data(self, **kwargs):
		context = super(RegistrarLineaCompra,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			lineacompra = form.save(commit=False)
			lineacompra.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class RegistrarIngrediente(CreateView):
	"""docstring for RegistrarCompra"""
	model = Ingrediente
	template_name = 'CrearIngrediente.html'
	form_class = IngredienteForm
	success_url = 'linea'

	def get_context_data(self, **kwargs):
		context = super(RegistrarIngrediente,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			ingrediente = form.save(commit=False)
			ingrediente.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarIngrediente(UpdateView):
	"""docstring for ActualizarIngrediente"""
	model = Ingrediente
	template_name = 'CrearIngrediente.html'
	form_class = IngredienteForm
	success_url = 'linea'

	def get_context_data(self, **kwargs):
		context = super(RegistrarIngrediente,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(self.request.POST)
		if form.is_valid():
			ingrediente = form.save(commit=False)
			ingrediente.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))


class EliminarCompra(DeleteView):
	"""docstring for Eliminar"""
	model = Compra
	template_name = 'EliminarCompra'

class EliminarLineaCompra(DeleteView):
	"""docstring for Eliminar"""
	model = LineaDeCompra
	template_name = 'EliminarLinea'

class EliminarIngrediente(DeleteView):
	"""docstring for Eliminar"""
	model = Ingrediente
	template_name = 'EliminarIngrediente'