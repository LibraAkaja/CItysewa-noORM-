"""
URL configuration for config project.
"""

# from django.contrib import admin
from django.urls import path, include
from rest_framework.renderers import JSONRenderer
from django.shortcuts import redirect
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)  

def homepage(request):
    return redirect("api/v1/docs")

urlpatterns = [
    path("", homepage, name="home-page"),
    path("api/v1/", include('src.api.urls')),
    path("api/v1/schema", SpectacularAPIView.as_view(renderer_classes=[JSONRenderer]), name="schema"),
    path("api/v1/docs", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui")
]
