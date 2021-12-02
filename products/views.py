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
    success_url = '/products/list/'
class ProductoListView(ListView):
    model = Producto
    template_name = "list_product.html"


class ProductoUpdateView(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "update_product.html"
    field = '__all__'
    success_url = '/products/list/'

#Para despues ...
class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = "delete_product.html"
    success_url = '/products/list/'


class ProductoDetailView(DetailView):
    model = Producto
    template_name = "detail_product.html"
