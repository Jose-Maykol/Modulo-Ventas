from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Venta
from .forms import VentaForm
# Create your views here.


class VentaCreateView(CreateView):
    model = Venta
    form_class = VentaForm
    template_name = "create_customer.html"
    success_url = '/'


class VentaListView(ListView):
    model = Venta
    template_name = "TEMPLATE_NAME"


class VentaUpdateView(UpdateView):
    model = Venta
    template_name = "TEMPLATE_NAME"


class VentaDetailView(DetailView):
    model = Venta
    template_name = "TEMPLATE_NAME"



    


