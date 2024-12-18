from django.urls import path
from .views import *


urlpatterns = [
    path('api/settings/', ParsingSettingsView.as_view(), name='parsing-settings'),
    path('api/values/', CryptoView.as_view(), name='values-crypto'),
]
