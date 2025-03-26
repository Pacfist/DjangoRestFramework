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
