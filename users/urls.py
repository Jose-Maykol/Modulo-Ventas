from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin.as_view(), name= 'login_user'),
    path('register/', views.userRegister.as_view(), name='register_user'),
]
