from django.db import models

# Create your models here.
class Host(models.Model):
    hostname = models.CharField(max_length=255, unique=True, verbose_name="主机名", blank=False)
    ip = models.GenericIPAddressField(max_length=255, verbose_name="IP地址", blank=False)
    disk = models.CharField(max_length=255, null=True, blank=True)
    cpu = models.CharField(max_length=255, null=True, blank=True)
    mem = models.CharField(max_length=255, null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hostname