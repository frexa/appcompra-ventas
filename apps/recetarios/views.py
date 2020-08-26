from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect
from apps.recetarios.forms import*
from apps.recetarios.models import*
from django.views.generic import*
from django.views.generic.detail import*

class RegistrarReceta(CreateView):
	"""docstring for RegistrarRecetas"""
	model= Receta
	template_name = 'receta_form.html'
	form_class = RecetaForm
	success_url = 'receta'

	def get_context_data(self, **kwargs):
		context = super(RegistrarReceta,self).get_context_data(**kwargs)
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
			
class ActualizarReceta(UpdateView):
	"""docstring for ActualizarRecetas"""
	model= Receta
	template_name = 'receta_form.html'
	fields = '__all__'

class EliminarRecetas(DeleteView):
	"""docstring for EliminarRecetas"""
	model = Receta
	template_name = 'receta_confirm_delete.html'
	success_url = reverse_lazy('recetas')

class RegistroElaboracion(CreateView):
	model = Elaboracion
	template_name = 'elaborar_pro.html'
	form_class = ElaborarForm
	success_url = 'formula'

	def get_context_data(self, **kwargs):
		context = super(RegistroElaboracion,self).get_context_data(**kwargs)
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

class ActualizarFormula(UpdateView):
	model = Elaboracion
	template_name = 'elaborar_pro.html'

class EliminarElaboracion(DeleteView):
	model = Elaboracion
	template_name = 'eliminar_elaboracion.html'
	success_url = reverse_lazy('elaboracion')

class ListarRecetas(ListView):
	model = Receta
	template_name = 'lista_receta.html'

class DetallesReceta(SingleObjectMixin,ListView):
	template_name = 'detalles_receta.html'
	paginate_by = 5
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object(queryset = Receta.objects.all())
		return super(DetallesReceta,self).get(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super(DetallesReceta,self).get_context_data(**kwargs)
		context['receta'] = self.object
		return context

	def get_queryset(self):
		return self.object.elaboracion_set.all()