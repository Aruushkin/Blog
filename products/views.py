from datetime import datetime

from django.shortcuts import render, redirect

from products.forms import ReviewForm, ProductForm
from products.models import Product, Category, Review


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context_data = {
            'products': products
        }
        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context_data = {
            'categories': categories
        }
        return render(request, 'categories/categories.html', context=context_data)


def product_detail_view(request, product_id):
    if request.method == 'GET':
        product = Product.objects.get(id=product_id)
        reviews = Review.objects.all()
        context_data = {
            'product': product,
            'reviews': reviews
        }
        return render(request, 'products/product_detail.html', context=context_data)


def add_review_view(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(pk=product_id)
        text = request.POST['text']
        Review.objects.create(product=product, text=text)
        return redirect('product_detail', product_id=product_id)  # Используйте 'product_id' здесь

    product = Product.objects.get(pk=product_id)
    return render(request, 'products/review.html', {'product': product})


def create_product_view(request):
    form = ProductForm()  # Инициализируем форму перед условием

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products_view')

    return render(request, 'products/create_product.html', {'form': form})


def create_category_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        Category.objects.create(name=name)
        return redirect('categories_view')  # Перенаправляем пользователя на страницу с категориями

    return render(request, 'products/create_category.html')

