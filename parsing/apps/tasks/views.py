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
        return Response({"Interval updated successfully"}, status=status.HTTP_201_CREATED)
     

class CryptoView(APIView):
    def get(self, request, *args, **kwargs):
        short_name = request.query_params.get('short_name')
        full_name = request.query_params.get('full_name')

        if short_name and full_name:
            return Response({"error": "Можно указать только один из параметров: short_name или full_name."}, 
                            status=status.HTTP_400_BAD_REQUEST)
        if not short_name and not full_name:
            return Response({"error": "Необходимо указать хотя бы один из параметров: short_name или full_name."}, 
                            status=status.HTTP_400_BAD_REQUEST)

        try:
            if short_name:
                entity = EntityCrypto.objects.get(short_name=short_name)
            else:
                entity = EntityCrypto.objects.get(full_name=full_name)
            values = ValuesCrypto.objects.filter(entity=entity)
            result = {}
            attributes = AttributeCrypto.objects.all()
            for attribute in attributes:
                latest_value = values.filter(attributes=attribute).order_by('-created_at').first()
                if latest_value:
                    result[attribute.name_attribute] = latest_value.values
            return Response({"status": "success", "data": result}, status=status.HTTP_200_OK)
        except EntityCrypto.DoesNotExist:
            return Response({"error": "EntityCrypto не найдено."}, status=status.HTTP_404_NOT_FOUND)