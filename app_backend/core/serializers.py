from rest_framework import serializers
from . import models

class CategorySerializer(serializers.ModelSerializer): 
    class Meta:
        models = models.Category
        fields = ('title', 'id', 'imageUrl')

class BrandSerializer(serializers.ModelSerializer): 
    class Meta:
        models = models.Brand
        fields = ('title', 'id', 'imageUrl')

class ProductSerializer(serializers.ModelSerializer): 
    class Meta:
        models = models.Product
        fields = '__all__'