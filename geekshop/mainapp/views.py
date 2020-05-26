import random

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def main(request):
    product_list = Product.objects.filter(is_enable=True, category__is_active=True).select_related('category')[:8]

    content = {
        'title': 'Главная',
        'products': product_list,
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None, page=1):
    if pk:
        product_list = Product.objects.filter(category__pk=pk).filter(is_enable=True)
        category = get_object_or_404(ProductCategory, pk=pk)
        content = {
            'title': category.alter_name,
            'category': category,
        }
    else:
        product_list = Product.objects.filter(is_enable=True, category__is_active=True)
        content = {
            'title': 'Каталог',
        }

    paginator = Paginator(product_list, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    content['products'] = products_paginator
    content['categories_menu_links'] = ProductCategory.objects.filter(is_active=True)

    return render(request, 'mainapp/products.html', context=content)


def sales(request):
    product_list = Product.objects.filter(is_enable=True).order_by('-quantity')[:5]
    content = {
        'title': 'Скидки',
        'products': product_list,
    }
    return render(request, 'mainapp/sales.html', context=content)


def product(request, pk):
    product = get_object_or_404(Product.objects.select_related(), pk=pk)
    same_products = Product.objects.filter(category=product.category).filter(is_enable=True).exclude(pk=pk).select_related()[:4]

    content = {
        'categories_menu_links': ProductCategory.objects.filter(is_active=True),
        'title': product.name,
        'product': product,
        'products': same_products,
    }
    return render(request, 'mainapp/product.html', context=content)


def contacts(request):
    content = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context=content)
