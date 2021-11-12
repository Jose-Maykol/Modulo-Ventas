from django.contrib import admin
from django.urls import path, include
from homepage.views import HomeView
from django.conf.urls.static import static 
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('products/', include('products.urls')),
    path('customers/', include('customers.urls')),
    path('sales/', include('sales.urls')),
    #path('bills/', include('bills.urls')),
    #path('orders/', include('orders.urls')),
    #path('vendors/', include('vendors.urls')),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)