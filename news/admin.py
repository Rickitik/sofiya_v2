from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Post, Graditude
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    # Подключаем форму виджета
    body = forms.CharField(label='Основной контент', widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image', 'publish', 'draft')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'title')  # Ссылка по имени и фамилии на основную запись
    list_filter = ('draft',)  # Фильтр по категории
    save_on_top = True  # Кнопка Сохранить наверху
    prepopulated_fields = {'url': ('title',)}  # Автозаполнение поля url
    form = PostAdminForm  # Подключение формы ркдактора

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

    get_image.short_description = 'Изображение'


@admin.register(Graditude)
class GraditudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_image', 'publish', 'draft')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'title')  # Ссылка по имени и фамилии на основную запись
    list_filter = ('draft',)  # Фильтр по категории
    save_on_top = True  # Кнопка Сохранить наверху
    prepopulated_fields = {'url': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

    get_image.short_description = 'Изображение'
