from django.urls import path
from . import views

urlpatterns = [
        path('', views.profile, name="user_profile"),
        path('products', views.profile, name="products"),

]