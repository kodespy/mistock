from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.http import HttpResponse

import json 


from .models import Moneda, Marca, Categoria, SubCategoria, Producto

from .forms import MonedaForm, MarcaForm, CategoriaForm, SubCategoriaForm,\
	ProductoForm

class MonedaView(LoginRequiredMixin, generic.ListView):
	model = Moneda
	template_name = "inv/moneda_list.html"
	context_object_name = "obj"
	login_url = "base:login"

class MonedaNew(LoginRequiredMixin, generic.CreateView):
	model = Moneda
	template_name = "inv/moneda_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MonedaForm
	success_url = reverse_lazy("inv:moneda_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class MonedaEdit(LoginRequiredMixin, generic.UpdateView):
	model = Moneda
	template_name = "inv/moneda_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MonedaForm
	success_url = reverse_lazy("inv:moneda_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)

class MonedaVer(LoginRequiredMixin, generic.UpdateView):
	model = Moneda
	template_name = "inv/moneda_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MonedaForm
	success_url = reverse_lazy("inv:moneda_list")



# def moneda_estado(request, pk, estado):
# 	moneda = Moneda.objects.filter(id=pk).first()
# 	contexto={}
# 	template_name="inv/catalogo_estado.html"
# 	if not moneda:
# 		return HttpResponse('No existe' + str(pk))
# 		#return redirect("inv:moneda_list")

# 	if request.method == 'GET':
# 		contexto={'obj': moneda}

# 	if request.method == 'POST':
# 		moneda.estado = estado
# 		moneda.save()
# 		contexto ={'obj': 'ok'}
# 		#return redirect("inv:moneda_list")
# 		return HttpResponse('Estado cambiado a' + str(pk))

# 	return render(request, template_name, contexto)	

def monedaEstado(request, pk, estado):
	moneda = Moneda.objects.filter(id=pk).first()
	contexto={}
	template_name="inv/moneda_estado.html"
	if not moneda:
		return redirect("inv:moneda_list")

	if request.method == 'GET':
		contexto={'obj': moneda}

	if request.method == 'POST':
		moneda.estado = estado
		moneda.save()
		contexto ={'obj': 'ok'}
		return redirect("inv:moneda_list")

	return render(request, template_name, contexto)	



class MarcaView(LoginRequiredMixin, generic.ListView):
	model = Marca
	template_name = "inv/marca_list.html"
	context_object_name = "obj"
	login_url = "base:login"

class MarcaNew(LoginRequiredMixin, generic.CreateView):
	model = Marca
	template_name = "inv/marca_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MarcaForm
	success_url = reverse_lazy("inv:marca_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class MarcaEdit(LoginRequiredMixin, generic.UpdateView):
	model = Marca
	template_name = "inv/marca_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MarcaForm
	success_url = reverse_lazy("inv:marca_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)

class MarcaVer(LoginRequiredMixin, generic.UpdateView):
	model = Marca
	template_name = "inv/marca_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = MarcaForm
	success_url = reverse_lazy("inv:marca_list")


def marcaEstado(request, pk, estado):
	marca = Marca.objects.filter(id=pk).first()
	contexto={}
	template_name="inv/marca_estado.html"
	if not marca:
		#return HttpResponse('No existe' + str(pk))
		return redirect("inv:marca_list")

	if request.method == 'GET':
		contexto={'obj': marca}

	if request.method == 'POST':
		marca.estado = estado
		marca.save()
		contexto ={'obj': 'ok'}
		#return HttpResponse('Estado cambiado a' + str(pk))
		return redirect("inv:marca_list")

	return render(request, template_name, contexto)	






class CategoriaView(LoginRequiredMixin, generic.ListView):
	model = Categoria
	template_name = "inv/categoria_list.html"
	context_object_name = "obj"
	login_url = "base:login"


class CategoriaNew(LoginRequiredMixin, generic.CreateView):
	model = Categoria
	template_name = "inv/categoria_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = CategoriaForm
	success_url = reverse_lazy("inv:categoria_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class CategoriaEdit(LoginRequiredMixin, generic.UpdateView):
	model = Categoria
	template_name = "inv/categoria_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = CategoriaForm
	success_url = reverse_lazy("inv:categoria_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)


class CategoriaVer(LoginRequiredMixin, generic.UpdateView):
	model = Categoria
	template_name = "inv/categoria_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = CategoriaForm
	success_url = reverse_lazy("inv:categoria_list")



class CategoriaDel(LoginRequiredMixin, generic.DeleteView):
	model = Categoria
	template_name = "inv/catalogo_estado.html"
	context_object_name = "obj"
	success_url = reverse_lazy("inv:categoria_list")

def categoriaEstado(request, pk, estado):
	categoria = Categoria.objects.filter(id=pk).first()
	contexto={}
	template_name="inv/categoria_estado.html"
	if not categoria:
		return redirect("inv:categoria_list")

	if request.method == 'GET':
		contexto={'obj': categoria}

	if request.method == 'POST':
		categoria.estado = estado
		categoria.save()
		contexto ={'obj': 'ok'}
		return redirect("inv:categoria_list")

	return render(request, template_name, contexto)	
		


class SubCategoriaView(LoginRequiredMixin, generic.ListView):
	model = SubCategoria
	template_name = "inv/subcategoria_list.html"
	context_object_name = "obj"
	login_url = "base:login"

class SubCategoriaNew(LoginRequiredMixin, generic.CreateView):
	model = SubCategoria
	template_name = "inv/subcategoria_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = SubCategoriaForm
	success_url = reverse_lazy("inv:subcategoria_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class SubCategoriaEdit(LoginRequiredMixin, generic.UpdateView):
	model = SubCategoria
	template_name = "inv/subcategoria_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = SubCategoriaForm
	success_url = reverse_lazy("inv:subcategoria_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)		

class SubCategoriaVer(LoginRequiredMixin, generic.UpdateView):
	model = SubCategoria
	template_name = "inv/subcategoria_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = SubCategoriaForm
	success_url = reverse_lazy("inv:subcategoria_list")



def subcategoriaEstado(request, pk, estado):
	subcategoria = SubCategoria.objects.filter(id=pk).first()
	contexto={}
	template_name="inv/subcategoria_estado.html"
	if not subcategoria:
		return redirect("inv:subcategoria_list")

	if request.method == 'GET':
		contexto={'obj': subcategoria}

	if request.method == 'POST':
		subcategoria.estado = estado
		subcategoria.save()
		contexto ={'obj': 'ok'}
		return redirect("inv:subcategoria_list")

	return render(request, template_name, contexto)	
		
class ProductoView(LoginRequiredMixin, generic.ListView):
	model = Producto
	template_name = "inv/producto_list.html"
	context_object_name = "obj"
	login_url = "base:login"		

class ProductoNew(LoginRequiredMixin, generic.CreateView):
	model = Producto
	template_name = "inv/producto_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProductoForm
	success_url = reverse_lazy("inv:producto_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		form.instance.existencia_actual = form.instance.existencia_inicial
		return super().form_valid(form)	

class ProductoEdit(LoginRequiredMixin, generic.UpdateView):
	model = Producto
	template_name = "inv/producto_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProductoForm
	success_url = reverse_lazy("inv:producto_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)				


class ProductoVer(LoginRequiredMixin, generic.UpdateView):
	model = Producto
	template_name = "inv/producto_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProductoForm
	success_url = reverse_lazy("inv:producto_list")

def productoEstado(request, pk, estado):
	producto = Producto.objects.filter(id=pk).first()
	contexto={}
	template_name="inv/producto_estado.html"
	if not producto:
		return redirect("inv:producto_list")

	if request.method == 'GET':
		contexto={'obj': producto}

	if request.method == 'POST':
		producto.estado = estado
		producto.save()
		contexto ={'obj': 'ok'}
		return redirect("inv:producto_list")

	return render(request, template_name, contexto)			