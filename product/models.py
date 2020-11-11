from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name=_('product name '))
    #category = models.CharField(max_length=100)
    PRDDesc = models.TextField(max_length=1000,verbose_name=_('product description'))
    PRDPrice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product price'))
    PRDCost = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product cost'))
    PRDCreated = models.DateTimeField(verbose_name=_('created at'))

    def __str__(self):
         return self.PRDName
 

class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_('product'))
    PRDIimag = models.ImageField(upload_to='product/' ,verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIproduct)
