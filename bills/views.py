from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Factura
from .forms import FacturaForm

# Create your views here.

class FacturaCreateView(CreateView):
    model = Factura
    form_class = FacturaForm
    template_name = "create_bill.html"
    success_url = '/bills/list/'

class FacturaListView(ListView):
    model = Factura
    template_name = "list_bill.html"

class FacturaUpdateView(UpdateView):
    model = Factura
    form_class = FacturaForm
    template_name = "update_bill.html"
    field = '__all__'
    success_url = '/bills/list/'

class FacturaDeleteView(DeleteView):
    model = Factura
    template_name = "delete_bill.html"
    success_url = '/bills/list/'

class FacturaDetailView(DetailView):
    model = Factura
    template_name = "detail_bill.html"
