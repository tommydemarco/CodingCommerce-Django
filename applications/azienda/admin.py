from django.contrib import admin

from .models import Tag, Category, Product, Employee

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Employee)