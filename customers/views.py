from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "create_customer.html"
    success_url = '/'


class ClienteListView(ListView):
    model = Cliente
    template_name = "list_customer.html"


class ClienteUpdateView(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "update_customer.html"
    field = '__all__'
    success_url = '/customers/list/'


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "delete_customer.html"
    success_url = '/customers/list/'



