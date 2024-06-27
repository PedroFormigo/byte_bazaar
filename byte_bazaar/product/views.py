from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from .models import Category, Product

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'

class ProductListByCategory(ListView):
    model = Product
    context_object_name = 'products'

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Product.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context