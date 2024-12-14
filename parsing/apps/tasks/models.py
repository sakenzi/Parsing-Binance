from django.db import models

# Create your models here.
class EntityCrypto(models.Model):
    short_name = models.CharField(max_length=150, null=False)
    full_name = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.short_name
    

class AttributeCrypto(models.Model):
    name_attribute = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.name_attribute
    

class ValuesCrypto(models.Model):
    values = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    entity = models.ForeignKey(EntityCrypto, on_delete=models.CASCADE, related_name='values')
    attributes = models.ForeignKey(AttributeCrypto, on_delete=models.CASCADE, related_name='values')