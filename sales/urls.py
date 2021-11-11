from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.VentaCreateView.as_view(), name= 'create_sale')
]
