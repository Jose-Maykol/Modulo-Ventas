from django import http
from django.shortcuts import redirect, render
from .models import Producto
from .forms import ProductoForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, detail
from django.urls import reverse_lazy
# Create your views here.


class ProductoCreateView(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "create_product.html"
    success_url = '/'
class ProductoListView(ListView):
    model = Producto
    template_name = "list_product.html"


class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = "TEMPLATE_NAME"

#Para despues ...
class ProductoDetailView(DetailView):
    model = Producto
    template_name = "TEMPLATE_NAME"
