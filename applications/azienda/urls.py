from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ProductsAPIList.as_view()),
    path('id/<id>/', views.ProductsAPIDetail.as_view())
]
