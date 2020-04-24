from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.compras.forms import*
from apps.compras.models import*

# Create your views here.

class RegistrarCompra(CreateView):
	"""docstring for RegistrarCompra"""
	model = Compra
	template_name = 'CrearCompra.html'
	form_class = CompraForm
	success_url = 'registar'

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
	template_name = 'resgistrarlineacompras.html'
	form_class = LineaDeCompraForm
	success_url = 'registar'

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
	template_name = 'resgistraringredientes.html'
	form_class = IngredienteForm
	success_url = 'registar'

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

