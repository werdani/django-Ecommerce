from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def product_list(request):
    product_list = Product.objects.all()
    
    paginator = Paginator(product_list, 4) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)

    return render(request,'product/product_list.html',{'product_list':product_list}) 



def product_detail(request,id):
    product_details = Product.objects.get(id=id)

    return render(request,'product/product_detail.html',{'product_details':product_details})