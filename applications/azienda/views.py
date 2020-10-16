from django.shortcuts import render
from rest_framework.generics import ListAPIView
#importing authentication from rest framework
from rest_framework.permissions import IsAuthenticated

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
    #applying uthentication to the class 
    permission_classes = (IsAuthenticated,)

    serializer_class = EmployeeSerializer
    
    def get_queryset(self):
        return Employee.objects.all()