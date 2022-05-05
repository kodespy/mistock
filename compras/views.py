from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic
from django.http import HttpResponse

import json 

from .models import Proveedor, Compras
from .forms import ProveedorForm

class ProveedorView(LoginRequiredMixin, generic.ListView):
	model = Proveedor
	template_name = "compras/proveedor_list.html"
	context_object_name = "obj"
	login_url = "base:login"

class ProveedorNew(LoginRequiredMixin, generic.CreateView):
	model = Proveedor
	template_name = "compras/proveedor_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProveedorForm
	success_url = reverse_lazy("compras:proveedor_list")

	def form_valid(self, form):
		form.instance.uc = self.request.user
		return super().form_valid(form)

class ProveedorEdit(LoginRequiredMixin, generic.UpdateView):
	model = Proveedor
	template_name = "compras/proveedor_form.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProveedorForm
	success_url = reverse_lazy("compras:proveedor_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)

class ProveedorVer(LoginRequiredMixin, generic.UpdateView):
	model = Proveedor
	template_name = "compras/proveedor_ver.html"
	context_object_name = "obj"
	login_url = "base:login"
	form_class = ProveedorForm
	success_url = reverse_lazy("compras:proveedor_list")

	def form_valid(self, form):
		form.instance.um = self.request.user.id
		return super().form_valid(form)
def proveedorEstado(request, pk, estado):
	proveedor = Proveedor.objects.filter(id=pk).first()
	contexto={}
	template_name="compras/proveedor_estado.html"
	if not proveedor:
		return redirect("compras:proveedor_list")

	if request.method == 'GET':
		contexto={'obj': proveedor}

	if request.method == 'POST':
		proveedor.estado = estado
		proveedor.save()
		contexto ={'obj': 'ok'}
		return redirect("compras:proveedor_list")

	return render(request, template_name, contexto)	


class ComprarView(LoginRequiredMixin, generic.ListView):
	model = Compras
	template_name = "compras/comprar_list.html"
	context_object_name = "obj"
	login_url = "base:login"