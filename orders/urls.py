from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.PedidoCreateView.as_view(), name= 'create_order'),
    path('list/', views.PedidoListView.as_view(), name='list_order'),
    path('edit/<int:pk>/', views.PedidoUpdateView.as_view(), name='update_order'),
    path('delete/<int:pk>/', views.PedidoDeleteView.as_view(), name='delete_order'),
]
