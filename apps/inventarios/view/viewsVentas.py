from django.shortcuts import render, get_object_or_404
from apps.inventarios.models import Venta
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.inventarios.forms.formVentas import VentasForm
# Create your views here.

class Registrar(CreateView):
	"""docstring for RegistrarVentas"""
	model= Venta
	template_name = 'Venta/venta_form.html'
	form_class = VentasForm
	success_url = 'ventas'

	def get_context_data(self, **kawargs):
		context = super(Registrar,self).get_context_data(**kawargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context

	def post(self, request, *args, **kawargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			venta = form.save(commit=False)
			venta.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))


class ActualizarVentas(UpdateView):
	"""docstring for ActualizarVentas"""
	model= Venta
	template_name = 'Venta/venta_form.html'
	fields = '__all__'

class EliminarIngrediente(DeleteView):
	"""docstring for EliminarVentas"""
	model = Venta
	template_name = 'Venta/venta_confirm_delete.html'
	success_url = reverse_lazy('ventas')