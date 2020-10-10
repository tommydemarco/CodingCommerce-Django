from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('applications.products.urls')),
    path('accounts/', include('applications.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
