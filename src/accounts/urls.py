from django.urls import path

from .views import (
    AdminRegisterAPIView,
    CustomerRegisterAPIView
)
urlpatterns= [
    path('admin/register', AdminRegisterAPIView.as_view(), name="admin-register"),
    path('customer/register', CustomerRegisterAPIView.as_view(), name="customer-register")
]