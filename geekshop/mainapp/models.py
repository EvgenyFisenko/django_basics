from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    alter_name = models.CharField(verbose_name='ru название для категории на сайте', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    is_active = models.BooleanField(verbose_name='Категория Активна', db_index=True, default=True)

    def __str__(self):
        return f'{self.name}({self.alter_name})'


class ProductBrand(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=64, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='brands_images', blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='Наименование', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True)
    characteristics = models.TextField(verbose_name='Характеристики')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    is_enable = models.BooleanField(verbose_name='Доступен', db_index=True, default=False)

    def __str__(self):
        return f"{self.name} {self.brand.name} ({self.category.name})"

    @staticmethod
    def get_items():
        return Product.objects.filter(is_enable=True).order_by('category', 'name')
