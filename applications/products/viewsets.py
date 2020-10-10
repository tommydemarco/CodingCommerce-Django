from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


'''=========> PRODUCT VIEW SETS '''

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #gets the products on sale and new with the help of the primary key
    @action(detail=True, methods=['get'])
    def sale(self, request, pk):
        queryset = Product.objects.filter(on_sale=True, new=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)
    
    #getting only products on sale without a primary key
    @action(detail=False)
    def onsale(self, request):
        on_sale_products = Product.objects.filter(on_sale=True)

        page = self.paginate_queryset(on_sale_products)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(on_sale_products, many=True)
        return Response(serializer.data)


'''=========> CATEGORY VIEW SETS '''

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    #getting all categories in a single result, not paginated
    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def products(self, request, pk):
        queryset = Product.objects.filter(category_id=pk)
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

