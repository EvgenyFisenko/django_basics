import random

from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.cache import never_cache

from geekshop import settings
from mainapp.models import Product, ProductCategory


def main(request):
    # product_list = Product.objects.filter(is_enable=True, category__is_active=True).select_related('category')[:8]
    products = get_products()[:8]

    content = {
        'title': 'Главная',
        'products': products,
    }
    return render(request, 'mainapp/index.html', context=content)


# @never_cache
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


def products_ajax(request, pk=None, page=1):
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

    result = render_to_string('mainapp/includes/inc_products_list_content.html', context=content, request=request)

    return JsonResponse({'result': result})


def sales(request):
    product_list = Product.objects.filter(is_enable=True).order_by('-quantity')[:5]
    content = {
        'title': 'Скидки',
        'products': product_list,
    }
    return render(request, 'mainapp/sales.html', context=content)


# @never_cache
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


def get_links_menu():
    if settings.LOW_CACHE:
        key = 'links_menu'
        links_menu = cache.get(key)
        if links_menu is None:
            links_menu = ProductCategory.objects.filter(is_active=True)
            cache.set(key, links_menu)
        return links_menu
    else:
        return ProductCategory.objects.filter(is_active=True)


def get_category(pk):
    if settings.LOW_CACHE:
        key = f'category_{pk}'
        category = cache.get(key)
        if category is None:
            category = get_object_or_404(ProductCategory, pk=pk)
            cache.set(key, category)
        return category
    else:
        return get_object_or_404(ProductCategory, pk=pk)


def get_products():
    if settings.LOW_CACHE:
        key = 'products'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_enable=True, category__is_active=True).select_related('category')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_enable=True, category__is_active=True).select_related('category')


def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product_{pk}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Product, pk=pk)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Product, pk=pk)


def get_products_orederd_by_price():
    if settings.LOW_CACHE:
        key = 'products_orederd_by_price'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(is_active=True, category__is_active=True).order_by('price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(is_active=True, category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
    if settings.LOW_CACHE:
        key = f'products_in_category_orederd_by_price_{pk}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by(
                'price')
            cache.set(key, products)
        return products
    else:
        return Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
