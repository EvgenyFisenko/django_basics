from django.contrib import admin
from mainapp.models import Product, ProductBrand, ProductCategory


admin.site.register(Product)
admin.site.register(ProductBrand)
admin.site.register(ProductCategory)

