from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.sections.urls')),
    path('api/', include('applications.products.urls'))
]
