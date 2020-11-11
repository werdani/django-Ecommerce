from django.db import models

# Create your models here.

class Product(models.Model):
    PRDName = models.CharField(max_length=100)
    #category = models.CharField(max_length=100)
    PRDDesc = models.TextField(max_length=1000)
    PRDPrice = models.DecimalField(max_digits=5,decimal_places=2)
    PRDCost = models.DecimalField(max_digits=5,decimal_places=2)
    PRDCreated = models.DateTimeField()



    def __str__(self):
         return self.PRDName
 


