from django.urls import path
from .views import *


urlpatterns = [
    path('api/settings/', ParsingSettingsView.as_view(), name='parsing-settings'),
]