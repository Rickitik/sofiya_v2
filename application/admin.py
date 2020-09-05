from django.contrib import admin
from .models import Application
from django.utils.safestring import mark_safe


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('id', 'fio', 'request_date')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'fio')  # Ссылка по имени и фамилии на основную запись
    save_on_top = True  # Кнопка Сохранить наверху

    def get_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.photo.url,
            width=obj.photo.width,
            height=obj.photo.height,
            ))

    get_image.short_description = 'Изображение'
