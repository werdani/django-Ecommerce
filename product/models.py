from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100 , verbose_name=_('product name '))
    # i used singlecote for category table becouse it is under product table .
    PRDcategory =models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("category"),blank=True, null=True)
    # to import settings app >>
    PRDBrand = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,verbose_name=_("Brand"),blank=True, null=True)
    PRDDesc = models.TextField(max_length=1000,verbose_name=_('product description'))
    PRDimag = models.ImageField(upload_to='product/' ,verbose_name=_("Image"),blank=True, null=True)
    PRDPrice = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product price'))
    PRDCost = models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_('product cost'))
    PRDCreated = models.DateTimeField(verbose_name=_('created at'))
    PRDSlug = models.SlugField(verbose_name=_("slug"),blank=True, null=True)
    class Meta:
        verbose_name = _("Product") # for single 
        verbose_name_plural = _("Products") # for collection

    ### def for slug 
    def save(self,*args,**kwargs):
        if not self.PRDSlug:
            self.PRDSlug = slugify(self.PRDName)
        super(Product,self).save(*args,**kwargs)


    def __str__(self):
         return self.PRDName
 

class ProductImage(models.Model):
    PRDIproduct = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_('product'))
    PRDIimag = models.ImageField(upload_to='product/' ,verbose_name=_("Image"))
    class Meta:
        verbose_name = _("ProductImage") # for single 
        verbose_name_plural = _("ProductImages") # for collection


    def __str__(self):
        return str(self.PRDIproduct)

class Category(models.Model):
    CATname = models.CharField(max_length=50,verbose_name=_("category name"))
    # self this is recersive relation ship . 
    # to view filter category main only i'am used  limit_choices_to .
    CATpearent = models.ForeignKey('self',limit_choices_to={'CATpearent__isnull':True},verbose_name=_("main category"),on_delete=models.CASCADE,blank=True, null=True)
    CATdesc = models.TextField(max_length=1000,verbose_name=_("category descereption"))
    CATimage = models.ImageField(upload_to='category/',verbose_name=_("category image"))
    class Meta:
        verbose_name = _("Category") # for single 
        verbose_name_plural = _("Categoryes") # for collection

    def __str__(self):
        return str(self.CATname)



class Product_Alternative (models.Model):
    PALNproduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='main_product',verbose_name=_("product"))
    PALNAlternative = models.ManyToManyField(Product,related_name='alternative_products',verbose_name=_("Alternatve"))
    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALNproduct)




class Product_Accessoris (models.Model):
    PACCproduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='mainACCESSORS_product',verbose_name=_("product"))
    PACCAlternative = models.ManyToManyField(Product,related_name='alternativeACCESSORS_products',verbose_name=_("Accessoris"))
    

    class Meta:
        verbose_name = _("Product Accessoris")
        verbose_name_plural = _("Product Accessoris")

    def __str__(self):
        return str(self.PACCproduct)








