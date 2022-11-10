from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from store import models

from category.models import Category
from store.models import Product


# Create your views here.

def store(request,category_slug = None):


    # if sub category is there like shirts/shoes/etc...
    if category_slug:
        categories = get_object_or_404(Category,slug = category_slug)
        products = models.Product.objects.all().filter(category = categories,is_available  = True)

    else:
        products = models.Product.objects.all().filter(is_available  = True)
    product_count = products.count()

    context = {
        "products" : products,
        "product_count":product_count
    }

    return render(request,'store/store.html',context = context)


def product_detail(request,category_slug = None,product_slug = None):

    try:
        single_product = Product.objects.get(category__slug = category_slug,slug = product_slug)
    except Exception as e:
        raise e

    context = {
        "single_product" : single_product
    }
    return render(request,'store/product_detail.html',context = context)
