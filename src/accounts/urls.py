from django.urls import path

from .views import CustomerRegisterAPIView

urlpatterns= [
    path('customer/register', CustomerRegisterAPIView.as_view(), name="customer-register")
]