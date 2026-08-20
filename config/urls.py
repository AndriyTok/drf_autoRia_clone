from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import health_check

urlpatterns = [
    path('admin', admin.site.urls),
    path('health', health_check, name='health-check'),
    path('api/v1/users', include('apps.users.urls')),
    path('api/v1/cars', include('apps.cars.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
