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

# def input_content(request):
#     return render(request, 'basic/input_content.html', {})

# def save_content(request):
#     image_path = request.POST['image_path']
#     blog_title = request.POST['blog_title']
#     blog_content = request.POST['blog_content']

#     bl = Blog(image_path=image_path, blog_title=blog_title, blog_content=blog_content)
#     bl.save()
#     blog = Blog.objects.all()
    
#     return render(request,'basic/blog.html', {'blog': blog}) 