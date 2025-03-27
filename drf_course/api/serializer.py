from rest_framework import serializers 

from .models import *


class BaseProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseProduct
        fields = (
            'name',
            'description'
        )
    def validate_name(self, value):
        if (value == "Pidor"):
            raise serializers.ValidationError(
                "Sam ty Pidor."
            )
        
        return value
        

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'full_name',
            'base_product',
            'color',
            'stock',
            'price',
            'memory',
            
        )


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            #'order',
            'product',
            'quantity',

        )

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = (
            'order_id',
            'created_at',
            'user',
            'status',
            'items',
        )
