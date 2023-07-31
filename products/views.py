from django.shortcuts import render


from products.models import Product, Category


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


def product_detail_view(request, id):
    if request.method == 'GET':
        products = Product.objects.get(id=id)
        context_data = {
            'product': products
        }

        return render(request, 'products/detail.html', context=context_data)

