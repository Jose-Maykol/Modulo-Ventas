from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import Pedido
from .forms import PedidoForm
# Create your views here.

class PedidoCreateView(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "create_order.html"
    success_url = '/orders/list/'

class PedidoListView(ListView):
    model = Pedido
    template_name = "list_order.html"


class PedidoUpdateView(UpdateView):
    model = Pedido
    form_class = PedidoForm
    field = '__all__'
    template_name = "update_order.html"
    success_url = '/orders/list/'

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = "delete_order.html"
    success_url = '/orders/list/'
