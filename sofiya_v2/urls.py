"""sofiya_v2 URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/', include('news.urls', namespace='news')),
    path('site/', include('site_custom.urls', namespace='site')),
    path('admin/', admin.site.urls),
    path('', include('child.urls', namespace='child'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
