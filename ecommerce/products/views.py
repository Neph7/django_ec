from django.shortcuts import render, redirect
from .models import  Category, Product
from .forms import  CategoryForm, ProductForm

def home(request):
    return render(request, "products/home.html")

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            # pass message
            return redirect("products:add_category")
    else:
        form = CategoryForm()
    return render(request,"products/category_form.html",{'form':form})

def category_list(request):
    categories = Category.objects.all()
    return render(request,"products/category_list.html",{'categories':categories})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products:add_product")
        else:
            form = ProductForm()
        return render(request,"products/product_list.html",{'form':form})

def get_products(request):
    products = Product.objects.all()
    return render(request,"products/products_list.html",{'products':products})

        

