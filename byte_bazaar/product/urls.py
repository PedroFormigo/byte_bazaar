from django.urls import path

from .views import CategoryList, ProductListByCategory, ProductDetail

app_name = 'product'

urlpatterns = [
    path('', CategoryList.as_view(), name='shop'),
    path('<slug:slug>/', ProductListByCategory.as_view(), name='product_list'),
    path('<slug:category_slug>/<slug:slug>', ProductDetail.as_view(), name='product_detail'),
]
