from django.shortcuts import render
from django.http import JsonResponse
from api.serializer import *
from api.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
# Createyourviews

@api_view(['GET'])
def baseProduct_list(request):
    baseProducts = BaseProduct.objects.all()
    serializer = BaseProductSerializer(baseProducts, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def products_list(request):
    
    temp = request.GET.get('name')
    products = Product.objects.filter(color__name=temp)
    if not products.exists():
        products = Product.objects.all()
    serializer = ProductSerializer(products, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    print(product)
    # print(product)
    # if not product.exists():
    #     product = Product.objects.all()
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many = True)
    return Response(serializer.data)