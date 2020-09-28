from django.urls import path, include

from .views import *

urlpatterns = [
    #home page view
    path('', HomeView.as_view(), name="home"),
]