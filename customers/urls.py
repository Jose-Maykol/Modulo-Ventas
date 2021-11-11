from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ClienteCreateView.as_view(), name= 'create_customer'),
    path('list/', views.ClienteListView.as_view(), name='list_customer'),
    path('edit/<int:pk>/', views.ClienteUpdateView.as_view(), name='update_customer'),
    path('delete/<int:pk>/', views.ClienteDeleteView.as_view(), name='delete_customer'),
]
