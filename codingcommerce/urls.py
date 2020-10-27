from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views as auth_views

#serving media files in development mode
from django.conf import settings 
from django.conf.urls.static import static


urlpatterns = [
    #=========> ADMIN
    path('admin/', admin.site.urls),
    #=========> API CONNECTION
    path('api/', include('applications.products.urls')),
    #=========> CMS 
    path('', include('applications.accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG == True: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
