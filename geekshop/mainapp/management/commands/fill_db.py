import os
import json

from django.core.management.base import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product, ProductBrand

JSON_PATH = 'mainapp/json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding="utf-8") as infile:
        return json.load(infile)


class Command(BaseCommand):
    help = 'Fill DB'

    def handle(self, *args, **options):
        categories = load_from_json('main_mainapp_productcategory')

        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()

        brands = load_from_json('main_mainapp_productbrand')

        ProductBrand.objects.all().delete()
        for brand in brands:
            new_brand = ProductBrand(**brand)
            new_brand.save()

        products = load_from_json('main_mainapp_product')

        Product.objects.all().delete()
        for product in products:
            category_name = product["category"]
            # Получаем категорию по имени
            _category = ProductCategory.objects.get(name=category_name)
            # Заменяем название категории объектом
            product['category'] = _category

            new_product = Product(**product)
            new_product.save()

        # ShopUser.objects.get(username="django", is_superuser=True).delete()
        super_user = ShopUser.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains', age=32)
