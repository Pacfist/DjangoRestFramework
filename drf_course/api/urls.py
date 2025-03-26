from django.urls import path
from . import views

urlpatterns = [
    path('base_products/', views.baseProduct_list),
    path('products/', views.products_list),
    path('products/<int:pk>', views.get_product),
]
