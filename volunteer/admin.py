from django.contrib import admin
from .models import Volunteer
from django.utils.safestring import mark_safe


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'get_image', 'email', 'Age', 'graduation')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'name')  # Ссылка по имени и фамилии на основную запись
    save_on_top = True  # Кнопка Сохранить наверху

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

    get_image.short_description = 'Изображение'
