from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Brand(models.Model):
    BRDName = models.CharField(max_length=50,verbose_name=_("brand name"))
    BRDDesc = models.TextField(blank=True, null=True,verbose_name=_("brand description"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.BRDName


class Variant(models.Model):
    VARName = models.CharField(max_length=50,verbose_name=_("variant name"))
    VARDesc = models.TextField(blank=True, null=True,verbose_name=_("variant description"))
    
    class Meta:
        verbose_name = _("Variant")
        verbose_name_plural = _("Variants")

    def __str__(self):
        return self.VARName

    