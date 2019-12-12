from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Product
from django.urls import reverse
# Create your views here.

def index(request):
    product = Product.objects.all()
    return render(request, 'liveapp/index.html', {'product': product})    

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'liveapp/detail.html', {'product': product})

def input_content(request):
    return render(request, 'liveapp/input_content.html', {})

def save_content(request):
    image_path = request.POST['image_path']
    product_name = request.POST['product_name']
    product_price = request.POST['product_price']
    product_desc = request.POST['product_desc']

    pr = Product(image_path=image_path, product_name=product_name, product_price=product_price, product_desc = product_desc)
    pr.save()
    product = Product.objects.all()
    
    return render(request,'liveapp/index.html', {'product': product}) 