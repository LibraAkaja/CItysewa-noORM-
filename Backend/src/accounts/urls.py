from django.urls import path

from .views import (
    AdminRegisterAPIView,
    AdminLoginAPIView,
    CustomerRegisterAPIView,
    CustomerLoginAPIView
)
urlpatterns= [
    path('admin/register', AdminRegisterAPIView.as_view(), name="admin-register"),
    path('admin/login', AdminLoginAPIView.as_view(), name="admin-login"),
    
    path('customer/register', CustomerRegisterAPIView.as_view(), name="customer-register"),
    path('customer/login', CustomerLoginAPIView.as_view(), name="customer-login"),
]