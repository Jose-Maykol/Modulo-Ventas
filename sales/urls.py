from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.VentaCreateView.as_view(), name= 'create_sale'),
    path('list/', views.VentaListView.as_view(), name='list_sale'),
    path('edit/<int:pk>/', views.VentaUpdateView.as_view(), name='update_sale'),
    path('delete/<int:pk>/', views.VentaDeleteView.as_view(), name='delete_sale'),
]
