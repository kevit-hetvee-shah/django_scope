from django.contrib import admin
from django.urls import path
from .views import GenerateScopeView
urlpatterns = [
    path('generate_scope', GenerateScopeView.as_view(), name="generate-scope"),
]
