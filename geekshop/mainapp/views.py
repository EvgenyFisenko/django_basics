import random

from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from basketapp.models import Basket


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def main(request):
    product_list = random.sample(list(Product.objects.filter(is_enable=True)), 8)
    content = {
        'title': 'Главная',
        'products': product_list,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    product_list = Product.objects.filter(is_enable=True)
    categories_menu_link = ProductCategory.objects.all()

    content = {
        'title': 'Каталог',
        'categories_menu_links': categories_menu_link,
        'products': product_list,
        'basket': get_basket(request.user),
    }
    if pk:
        product_list = Product.objects.filter(category__pk=pk).filter(is_enable=True)
        content['products'] = product_list
        category = get_object_or_404(ProductCategory, pk=pk)
        content['title'] = category.alter_name
    return render(request, 'mainapp/products.html', context=content)


def sales(request):
    product_list = Product.objects.filter(is_enable=True).order_by('-quantity')[:5]
    content = {
        'title': 'Скидки',
        'products': product_list,
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/sales.html', context=content)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    same_products = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]

    content = {
        'categories_menu_links': ProductCategory.objects.all(),
        'title': product.name,
        'product': product,
        'basket': get_basket(request.user),
        'products': same_products,
    }
    return render(request, 'mainapp/product.html', context=content)


def contacts(request):
    content = {
        'title': 'Контакты',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contacts.html', context=content)
