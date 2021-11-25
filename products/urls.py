from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ProductoCreateView.as_view(), name= 'create_product'),
    path('list/', views.ProductoListView.as_view(), name='list_product'),
    path('edit/<int:pk>/', views.ProductoUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', views.ProductoDeleteView.as_view(), name='delete_product'),
    path('detail/<int:pk>/', views.ProductoDetailView.as_view(), name='detail_product'),
]
