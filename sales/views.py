from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Venta
from .forms import VentaForm
# Create your views here.


class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = "create_sale.html"
    success_url = '/'


class VentaListView(ListView):
    model = Venta
    template_name = "list_sale.html"


class VentaUpdateView(UpdateView):
    model = Venta
    form_class = VentaForm
    field = '__all__'
    template_name = "update_sale.html"
    success_url = '/sales/list/'


class VentaDeleteView(DeleteView):
    model = Venta
    template_name = "delete_sale.html"
    success_url = '/sales/list/'



    


