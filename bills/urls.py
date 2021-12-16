from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.FacturaCreateView.as_view(), name= 'create_bill'),
    path('list/', views.FacturaListView.as_view(), name='list_bill'),
    path('edit/<int:pk>/', views.FacturaUpdateView.as_view(), name='update_bill'),
    path('delete/<int:pk>/', views.FacturaDeleteView.as_view(), name='delete_bill'),
    path('detail/<int:pk>/', views.FacturaDetailView.as_view(), name='detail_bill'),
]
