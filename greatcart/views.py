from django.shortcuts import render

from store import models


def home(request):
    products = models.Product.objects.all().filter(is_available  = True)
    
    return render(request,'home.html',{"products":products})