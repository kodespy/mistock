from re import template
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin

from django.views import generic

from .models import Empresa
from .forms import EmpresaForm


class Home(LoginRequiredMixin, generic.TemplateView):
    template_name = 'home.html'
    login_url = 'base:login'


class EmpresaView(LoginRequiredMixin, generic.ListView):
    model = Empresa
    template_name = "empresa_list.html"
    context_object_name = "obj"
    login_url = "base:login"
