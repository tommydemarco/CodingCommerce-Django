from django.contrib import admin

from .models import Tag, Category, Product, Employee, Article

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Employee)
admin.site.register(Article)