from django.shortcuts import render
from django.http import JsonResponse
from api.serializer import BaseProductSerializer, ProductSerializer
from api.models import BaseProduct, Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

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
    products = Product.objects.filter(id=pk)
    if not products.exists():
        products = Product.objects.all()
    serializer = ProductSerializer(products)
    return Response(serializer.data)

