from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.


class ParsingSettingsView(APIView):
    def get(self, request):
        settings= ParsingSettings.objects.first()
        if settings:
            serializer = ParisngSettingsSerializer(settings)
            return Response(serializer.data)
        return Response({"error":"Settings not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        data = request.data
        settings, created = ParsingSettings.objects.get_or_create(id=1)
        settings.interval_minutes = data.get('interval_minutes', settings.interval_minutes)
        settings.save()
        return Response({"error": "Interval updated successfully"}, status=status.HTTP_201_CREATED) 