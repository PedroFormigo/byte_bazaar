from django.urls import path

from .views import CategoryList, ProductListByCategory

app_name = 'product'

urlpatterns = [
    path('', CategoryList.as_view(), name='shop'),
    path('<slug:slug>/', ProductListByCategory.as_view(), name='product_list')
]
