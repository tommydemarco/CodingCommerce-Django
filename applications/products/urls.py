from django.urls import path, include
from rest_framework import routers
from .viewsets import ProductViewSet, CategoryViewSet

route = routers.SimpleRouter()
route.register('product', ProductViewSet)
route.register('category', CategoryViewSet)

urlpatterns = route.urls