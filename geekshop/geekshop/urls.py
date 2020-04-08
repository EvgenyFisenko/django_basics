"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from mainapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/phones/', views.catalog_phones, name='catalog_phones'),
    path('catalog/smartphones/', views.catalog_smartphones, name='catalog_smartphones'),
    path('catalog/tablets/', views.catalog_tablets, name='catalog_tablets'),
    path('catalog/accessories/', views.catalog_accessories, name='catalog_accessories'),
    path('sales/', views.sales, name='sales'),
    path('product/', views.product, name='product'),
    path('contacts/', views.contacts, name='contacts'),
]
