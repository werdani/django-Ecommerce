from django.shortcuts import render
from . models import Product

# Create your views here.

def product_list(request):
    product_list = Product.objects.all()

    return render(request,'product/product_list.html',{'product_list':product_list}) 



def product_detail(request,id):
    product_details = Product.objects.get(id=id)

    return render(request,'product/product_detail.html',{'product_details':product_details})