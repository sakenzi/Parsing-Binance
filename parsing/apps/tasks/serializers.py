from rest_framework import serializers
from .models import *


class EntityCryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntityCrypto
        fields = ['short_name','full_name']


class AttributeCryptoSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributeCrypto
        fields = ['name_attribute']

    
class ValuesCryptoSerializer(serializers.ModelSerializer):
    entity = EntityCryptoSerializer
    attributes = AttributeCryptoSerializer

    class Meta:
        model = ValuesCrypto
        fields = ['values','created_at','entity','attributes']


class ParisngSettingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParsingSettings
        fields = ['interval_minutes']