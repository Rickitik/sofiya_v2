"""sofiya_v2 URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Администрирование данных фонда"
admin.site.site_title = "Фонд поддержки детей им. А.Ф. Романовой"
admin.site.index_title = "Основные приложения"

urlpatterns = [
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('posts/', include('news.urls', namespace='news')),
    path('site/', include('site_custom.urls', namespace='site')),
    path('team/', include('team.urls', namespace='team')),
    path('volunteer/', include('volunteer.urls', namespace='volunteer')),
    path('application/', include('application.urls', namespace='application')),
    path('admin/', admin.site.urls),
    path('', include('child.urls', namespace='child'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
