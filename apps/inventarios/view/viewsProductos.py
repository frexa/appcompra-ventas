from django.shortcuts import render, get_object_or_404
from apps.inventarios.models import Producto
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.inventarios.forms.formProducto import ProductoForm

class Registrar(CreateView):
	"""docstring for RegistrarProductos"""
	model= Producto
	template_name = 'Producto/producto_form.html'
	form_class = ProductoForm
	success_url = 'lista/productos'

	def get_context_data(self, **kwargs):
		context = super(Registrar,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			producto = form.save(commit=False)
			producto.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))

class ActualizarProductos(UpdateView):
	"""docstring for ActualizarProductos"""
	model= Producto
	template_name = 'Producto/producto_form.html'
	fields = '__all__'

class EliminarProductos(DeleteView):
	"""docstring for EliminarProductos"""
	model = Producto
	template_name = 'Producto/producto_confirm_delete.html'
	success_url = reverse_lazy('productos')