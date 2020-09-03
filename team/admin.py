from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe
from .models import Team, PersonFilesDocuments
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TeamAdminForm(forms.ModelForm):
	# Подключаем форму виджета
	history = forms.CharField(label='История сотрудника', widget=CKEditorUploadingWidget())

	class Meta:
		model = Team
		fields = '__all__'


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
	list_display = ('fio', 'position', 'get_image')
	readonly_fields = ('get_image',)
	list_display_links = ('fio', 'position')
	save_on_top = True
	prepopulated_fields = {'url': ('fio',)}
	form = TeamAdminForm

	def get_image(self, obj):
		return mark_safe(f'<img src={obj.photo.url} width="50", height="60">')

	get_image.short_description = 'Изображение'


admin.site.register(PersonFilesDocuments)
