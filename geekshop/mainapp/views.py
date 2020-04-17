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


def products(request, category_id=None):
    product_list = Product.objects.filter(is_enable=True)
    categories_menu_link = ProductCategory.objects.all()

    content = {
        'title': 'Каталог',
        'categories_menu_links': categories_menu_link,
        'products': product_list,
        'basket': get_basket(request.user),
    }
    if category_id:
        product_list = Product.objects.filter(category__id=category_id).filter(is_enable=True)
        content['products'] = product_list
        category = get_object_or_404(ProductCategory, pk=category_id)
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


def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category = get_object_or_404(ProductCategory, pk=category_id)
    categories_menu_link = ProductCategory.objects.all()
    same_products = Product.objects.filter(category=category_id).exclude(pk=product_id)[:4]

    content = {
        'categories_menu_links': categories_menu_link,
        'title': product.name,
        'category': category,
        'product': product,
        'basket': get_basket(request.user),
        'products': same_products,
    }
    return render(request, 'mainapp/product_detail.html', context=content)


def contacts(request):
    content = {
        'title': 'Контакты',
        'basket': get_basket(request.user),
    }
    return render(request, 'mainapp/contacts.html', context=content)
