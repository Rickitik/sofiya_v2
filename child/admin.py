from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Child
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ChildAdminForm(forms.ModelForm):
    # Подключаем форму виджета
    history = forms.CharField(label='История ребенка', widget=CKEditorUploadingWidget())

    class Meta:
        model = Child
        fields = '__all__'


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id', 'surname', 'name', 'birthday', 'get_image', 'status', 'publicated_on_site')
    readonly_fields = ('get_image',)
    list_display_links = ('id', 'surname', 'name')  # Ссылка по имени и фамилии на основную запись
    list_filter = ('status', 'publicated_on_site',)  # Фильтр по категории
    list_editable = ('publicated_on_site',)
    search_fields = ('surname', 'name')
    save_on_top = True  # Кнопка Сохранить наверху
    prepopulated_fields = {'url': ('surname', 'name', 'birthday',)}  # Автозаполнение поля url
    form = ChildAdminForm  # Подключение формы редактора
    fieldsets = (
        (None, {
            "fields": (("name", "name_rod", "surname", "lastname"),)
        }),
        (None, {
            "fields": (("birthday", "age"),)
        }),
        (None, {
            "fields": ("place",)
        }),
        (None, {
            "fields": ("problem",)
        }),
        (None, {
            "fields": ("history",)
        }),
        (None, {
            "fields": (("photo", 'get_image'),)
        }),
        (None, {
            "fields": (("status","money_need", "money_collected"),)
        }),
        (None, {
            "fields": ("problem_solution",)
        }),
        (None, {
            "fields": (("url", "publicated_on_site"),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

    get_image.short_description = 'Изображение'
