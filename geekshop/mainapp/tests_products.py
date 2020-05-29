from django.test import TestCase
from mainapp.models import Product, ProductCategory, ProductBrand


class ProductsTestCase(TestCase):
    def setUp(self):
        category = ProductCategory.objects.create(name="смартфоны")
        brand = ProductBrand.objects.create(name="iphone")
        self.product_1 = Product.objects.create(name="6",
                                                category=category,
                                                brand=brand,
                                                price=1999.5,
                                                quantity=150,
                                                is_enable=True)

        self.product_2 = Product.objects.create(name="7",
                                                category=category,
                                                brand=brand,
                                                price=2998.1,
                                                quantity=125,
                                                is_enable=False)

        self.product_3 = Product.objects.create(name="8",
                                                category=category,
                                                brand=brand,
                                                price=998.1,
                                                quantity=115,
                                                is_enable=True)

    def test_product_get(self):
        product_1 = Product.objects.get(name="6")
        product_2 = Product.objects.get(name="7")
        self.assertEqual(product_1, self.product_1)
        self.assertEqual(product_2, self.product_2)

    def test_product_print(self):
        product_1 = Product.objects.get(name="6")
        product_2 = Product.objects.get(name="7")
        self.assertEqual(str(product_1), '6 iphone (смартфоны)')
        self.assertEqual(str(product_2), '7 iphone (смартфоны)')

    def test_product_get_items(self):
        product_1 = Product.objects.get(name="6")
        product_3 = Product.objects.get(name="8")
        products = product_1.get_items()

        self.assertEqual(list(products), [product_1, product_3])
