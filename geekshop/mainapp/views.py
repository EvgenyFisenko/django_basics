from django.shortcuts import render


MAIN_MENU_LINKS = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'catalog', 'name': 'Каталог'},
    {'href': 'sales', 'name': 'Скидки'},
    {'href': 'contacts', 'name': 'Контакты'},
]

CATEGORIES_MENU_LINKS = [
    {'href': 'catalog', 'name': 'Все'},
    {'href': 'catalog_phones', 'name': 'Телефоны'},
    {'href': 'catalog_smartphones', 'name': 'Смартфоны'},
    {'href': 'catalog_tablets', 'name': 'Планшеты'},
    {'href': 'catalog_accessories', 'name': 'Аксессуары'},
]


def main(request):
    content = {
        'top_products_count': list(range(4)),
        'sale_products_count': list(range(4)),
        'title': 'Главная',
        'main_menu_links': MAIN_MENU_LINKS,
    }
    return render(request, 'mainapp/index.html', context=content)


def catalog(request):
    content = {
        'products_count': list(range(10)),
        'title': 'Каталог',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/catalog.html', context=content)


def catalog_phones(request):
    content = {
        'products_count': list(range(9)),
        'title': 'Телефоны',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/catalog.html', context=content)


def catalog_smartphones(request):
    content = {
        'products_count': list(range(7)),
        'title': 'Смартфоны',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/catalog.html', context=content)


def catalog_tablets(request):
    content = {
        'products_count': list(range(6)),
        'title': 'Планшеты',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/catalog.html', context=content)


def catalog_accessories(request):
    content = {
        'products_count': list(range(5)),
        'title': 'Аксессуары',
        'main_menu_links': MAIN_MENU_LINKS,
        'categories_menu_links': CATEGORIES_MENU_LINKS,
    }
    return render(request, 'mainapp/catalog.html', context=content)


def sales(request):
    content = {
        'products_count': list(range(7)),
        'title': 'Скидки',
        'main_menu_links': MAIN_MENU_LINKS,
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
