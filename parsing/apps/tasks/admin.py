from django.contrib import admin
from .models import *


class EntityCryptoAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'full_name')
    search_fields = ('short_name', 'full_name')
    ordering = ('-id',)


class AttributeCryptoAdmin(admin.ModelAdmin):
    list_display = ('name_attribute',)
    search_fields = ('name_attribute',)
    ordering = ('-id',)


class ValuesCryptoAdmin(admin.ModelAdmin):
    list_display = ('entity', 'attributes', 'values', 'created_at')
    search_fields = ('values', 'entity__short_name', 'attributes__name_attribute')
    list_filter = ('created_at', 'entity', 'attributes')
    ordering = ('-id',)


class ParsingSettingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'interval_minutes')


admin.site.register(EntityCrypto, EntityCryptoAdmin)
admin.site.register(AttributeCrypto, AttributeCryptoAdmin)
admin.site.register(ValuesCrypto, ValuesCryptoAdmin)
admin.site.register(ParsingSettings, ParsingSettingsAdmin)