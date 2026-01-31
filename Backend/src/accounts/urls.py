from django.urls import path

from .views import (
    AdminRegisterAPIView,
    AdminLoginAPIView,
    CustomerRegisterAPIView,
    CustomerLoginAPIView,
    CustomerListAPIView,
    CustomerRetrieveAPIView,
    ProviderRegisterAPIView,
    ProviderLoginAPIView,
    ProviderListAPIView,
    ProviderRetrieveAPIView,
    ProviderSubmitVerificationAPIView,
    VerificationListAPIView,
    VerificationRetrieveAPIView,
)
urlpatterns= [
    path('admin/register', AdminRegisterAPIView.as_view(), name="admin-register"),
    path('admin/login', AdminLoginAPIView.as_view(), name="admin-login"),
    
    path('customer/register', CustomerRegisterAPIView.as_view(), name="customer-register"),
    path('customer/login', CustomerLoginAPIView.as_view(), name="customer-login"),
    path('customer', CustomerListAPIView.as_view(), name="customer-list"),
    path('customer/<int:id>', CustomerRetrieveAPIView.as_view(), name="customer-retrieve"),
    
    path('provider/register', ProviderRegisterAPIView.as_view(), name="provider-register"),
    path('provider/login', ProviderLoginAPIView.as_view(), name="provider-login"),
    path('provider', ProviderListAPIView.as_view(), name="provider-list"),
    path('provider/<int:id>', ProviderRetrieveAPIView.as_view(), name="provider-retrieve"),
    path('provider/submit-verification', ProviderSubmitVerificationAPIView.as_view(), name="provider-submit-verification"),
    
    path("provider/verification-data", VerificationListAPIView.as_view(), name="verification-data-list"),
    path("provider/verification-data/<int:id>", VerificationRetrieveAPIView.as_view(), name="verification-data-retrieve"),
]