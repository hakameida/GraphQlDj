from rest_framework import serializers
from .models import Laptop
from .models import Product
class LaptopMinimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        fields = ['id', 'model_name', 'price_syp', 'price_usd', 'main_image']  # Added 'id'

class LaptopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Laptop
        exclude = ['main_image']  # This removes the main image from the response



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
