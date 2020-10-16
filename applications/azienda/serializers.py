from rest_framework import serializers
from .models import Product, Category, Tag, Employee, Article

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Product 
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        