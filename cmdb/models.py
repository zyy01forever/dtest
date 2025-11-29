from django.db import models

# Create your models here.

class Host(models.Model):
    hostname = models.CharField(max_length=255, verbose_name="主机名", unique=True, blank=False)
    ip = models.GenericIPAddressField(verbose_name="IP地址", blank=False)
    disk = models.TextField(verbose_name="磁盘信息", null=True, blank=True)
    mem = models.TextField(verbose_name="内存信息", null=True, blank=True)
    cpu = models.TextField(verbose_name="CPU信息", null=True, blank=True)
    desc = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.hostname