from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import *
from .serializers import *

# Create your views here.

class ProductsAPIList(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        return Product.objects.all()

class ProductsAPIDetail(ListAPIView):
    serializer_class = ProductSerializer
    
    def get_queryset(self):
        id = self.kwargs['id']
        return Product.objects.filter(id=id)

class EmployeeAPIList(ListAPIView):
    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        return Employee.objects.all()