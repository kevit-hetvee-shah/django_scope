from django.contrib import admin
from django.urls import path
from .views import GenerateScopeView, ms_login, ms_callback
urlpatterns = [
    path('', GenerateScopeView.as_view(), name="generate-scope"),
    path('ms_login', ms_login, name="ms_login"),
    path('msal/callback/', ms_callback, name='ms_callback'),
]
