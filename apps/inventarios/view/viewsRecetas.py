from django.shortcuts import render, get_object_or_404
from apps.inventarios.models import Receta
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.inventarios.forms.formReceta import RecetaForm

class Registrar(CreateView):
	"""docstring for RegistrarRecetas"""
	model= Receta
	template_name = 'Receta/receta_form.html'
	form_class = RecetaForm
	success_url = 'receta'

	def get_context_data(self, **kwargs):
		context = super(Registrar,self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form']=self.form_class(request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object= self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			receta = form.save(commit=False)
			receta.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return render_to_response(self.get_context_data(form=form))
			
class ActualizarRecetas(UpdateView):
	"""docstring for ActualizarRecetas"""
	model= Receta
	template_name = 'Receta/receta_form.html'
	fields = '__all__'

class EliminarRecetas(DeleteView):
	"""docstring for EliminarRecetas"""
	model = Receta
	template_name = 'Receta/receta_confirm_delete.html'
	success_url = reverse_lazy('recetas')