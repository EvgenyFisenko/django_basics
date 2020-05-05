from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserListView(ListView):
    model = ShopUser
    template_name = "adminapp/users.html"


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserCreateView(CreateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy('admin:users')
    fields = ('username', 'first_name', 'email', 'age', 'avatar', 'password', 'is_active', 'is_superuser')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = "adminapp/user_update.html"
    success_url = reverse_lazy('admin:users')
    fields = '__all__'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = "adminapp/user_delete.html"
    success_url = reverse_lazy('admin:users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryListView(ListView):
    model = ProductCategory
    template_name = "adminapp/categories.html"


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy('adminapp:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Создать категорию'
        return context


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактировать категорию'
        return context


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"
    success_url = reverse_lazy('admin:categories')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = "adminapp/products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(ProductCategory, pk=self.kwargs['pk'])
        context['title'] = 'админка/продукты'
        return context
    
    def get_queryset(self):
        return Product.objects.filter(category__pk=self.kwargs['pk']).order_by('name')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    template_name = "adminapp/product_update.html"
    fields = '__all__'

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['category'] = self.kwargs['pk']
        return initial_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['pk']
        context['title'] = 'aдминка/создать продукт'
        return context

    def get_success_url(self):
        return reverse_lazy('admin:products', kwargs={'pk': self.kwargs['pk']})


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductDetailView(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductUpdateView(UpdateView):
    model = Product
    template_name = "adminapp/product_update.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_object().category.pk
        context['title'] = 'aдминка/изменить продукт'
        return context
    
    def get_success_url(self):
        return reverse_lazy('admin:products', kwargs={'pk': self.get_object().category.pk})


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class ProductDeleteView(DeleteView):
    model = Product
    template_name = "adminapp/product_delete.html"

    def get_success_url(self):
        return reverse_lazy('admin:products', kwargs={'pk': self.get_object().category.pk})

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_enable = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
