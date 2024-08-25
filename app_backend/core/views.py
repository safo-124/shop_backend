from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models, serializers
from django.db.models import Count
import random

# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    queryset = models.Category.objects.all()

class HomeCategoryList(generics.ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        
        queryset = models.Category.objects.all();
        queryset = queryset.annotate(random_order=Count('id'))

        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:5]
    
class BrandList(generics.ListAPIView):
    serializer_class = serializers.BrandSerializer

    queryset = models.Brand.objects.all()

class ProductList(generics.ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        
        queryset = models.Category.objects.all();
        queryset = queryset.annotate(random_order=Count('id'))

        queryset = list(queryset)
        random.shuffle(queryset)

        return queryset[:5]