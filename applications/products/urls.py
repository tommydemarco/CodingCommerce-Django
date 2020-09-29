from django.urls import path, include

from .views import *

urlpatterns = [
    #home page view
    path('', HomeView.as_view(), name="home"),
    path('api/products/list/', ProductsAPIListView.as_view(), name="home"),
]