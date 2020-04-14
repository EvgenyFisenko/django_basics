from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def main(request):
    product_list = Product.objects.filter(is_enable=True)[:8]
    content = {
        'title': 'Главная',
        'products': product_list
    }
    return render(request, 'mainapp/index.html', context=content)


def products(request, category_id=None):
    product_list = Product.objects.filter(is_enable=True)
    categories_menu_link = ProductCategory.objects.all()

    content = {
        'title': 'Каталог',
        'categories_menu_links': categories_menu_link,
        'products': product_list,
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
    }
    return render(request, 'mainapp/sales.html', context=content)


def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category = get_object_or_404(ProductCategory, pk=category_id)
    categories_menu_link = ProductCategory.objects.all()

    content = {
        'categories_menu_links': categories_menu_link,
        'title': product.name,
        'category': category,
        'product': product,
    }
    return render(request, 'mainapp/product_detail.html', context=content)


def contacts(request):
    content = {
        'title': 'Контакты',
    }
    return render(request, 'mainapp/contacts.html', context=content)
