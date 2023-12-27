from django.shortcuts import render
from.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def Product(request, id):
    cata = catagory.objects.get(id=id)
    Product_all = product.objects.filter(catagory=cata)
    # Number of items per page
    items_per_page = 10  # You can set the number of items you want per page

    paginator = Paginator(Product_all, items_per_page)
    page = request.GET.get('page')
 
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        products = paginator.page(paginator.num_pages)
        
    return render(request, 'Product/Product.html',{'products': products, 'category': cata})
    

