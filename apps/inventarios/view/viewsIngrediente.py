from django.shortcuts import render, get_object_or_404, redirect
from apps.inventarios.models import Ingrediente
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.inventarios.forms.formIngrediente import IngredienteForm
# Create your views here.

class Registrar(CreateView):
	"""docstring for RegistrarIngredientes"""
	model = Ingrediente
	form_class = IngredienteForm
	template_name = 'Ingrediente/registrar.html'
	success_url = 'registrar/ingrediente'

	def get_context_data(self, **kwargs):
		context = super(Registrar, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		return context
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		if form.is_valid():
			ingrediente = form.save(commit = False)
			ingrediente.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form = form))

class ActualizarIngrediente(UpdateView):
	"""docstring for ActualizarIngredientes"""
	model= Ingrediente
	template_name = 'Ingrediente/ingrediente_form.html'
	fields = '__all__'

class EliminarIngrediente(DeleteView):
	"""docstring for EliminarIngredientes"""
	model = Ingrediente
	template_name = 'Ingrediente/ingrediente_confirm_delete.html'
	success_url = reverse_lazy('ingredientes')

class ListaIngrediente(generic.ListView):
	"""docstring for ConsultarIngrediente"""
	model= Ingrediente
	paginate_by=3
	template_name = 'Ingrediente/ingrediente_list.html'

	def get_context_data(self, **kwargs):
		context= super(ListaIngrediente,self).get_context_data(**kwargs)
		context['some_data'] = 'This is just some data'
		return context
	def get_queryset(self):
		return Ingrediente.objects.all().order_by('nombre')

class DetallesIngrediente(generic.DetailView):
	model=Ingrediente
	template_name='Ingrediente/ingrediente_detail.html'

class InventarioIngredientes(generic.ListView):
	model = Ingrediente
	template_name = 'Ingrediente/inventario.html'
	paginate_by = 5