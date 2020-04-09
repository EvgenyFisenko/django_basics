from django.shortcuts import render
from mainapp.models import Product, ProductCategory


MAIN_MENU_LINKS = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'products:index', 'name': 'Каталог'},
    {'href': 'sales', 'name': 'Скидки'},
    {'href': 'contacts', 'name': 'Контакты'},
]

CATEGORIES_MENU_LINKS = ProductCategory.objects.all()


def main(request):
    product_list = Product.objects.all()[:8]
    content = {
        'title': 'Главная',
        'main_menu_links': MAIN_MENU_LINKS,
        'products': product_list
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, pk=None):
    product_list = Product.objects.all()
    content = {
        'title': 'Каталог',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
        'products': product_list,
    }
    if pk:
        product_list = Product.objects.filter(category__id=pk)
        content['products'] = product_list
        category = ProductCategory.objects.get(pk=pk)
        content['title'] = category.alter_name
    return render(request, 'mainapp/products.html', context=content)


def sales(request):
    product_list = Product.objects.all().order_by('-quantity')[:5]
    content = {
        'title': 'Скидки',
        'main_menu_links': MAIN_MENU_LINKS,
        'products': product_list,
    }
    return render(request, 'mainapp/sales.html', context=content)


def product(request):
    content = {
        'title': 'Производитель Модель',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/product.html', context=content)


def contacts(request):
    content = {
        'title': 'Контакты',
        'main_menu_links': MAIN_MENU_LINKS,
    }
    return render(request, 'mainapp/contacts.html', context=content)
