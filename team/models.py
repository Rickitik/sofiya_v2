from django.db import models
from django.urls import reverse


class Team(models.Model):
	"""Данные сотрудника"""
	fio = models.CharField('ФИО', max_length=100)
	position = models.CharField('Должность', max_length=100)
	photo = models.ImageField('Изображение', upload_to='team_photo')
	history = models.TextField('История сотрудника')
	url = models.SlugField(max_length=130, unique=True)

	def __str__(self):
		return self.fio

	def get_absolute_url(self):
		return reverse('team:team_detail', kwargs={'slug': self.url})

	class Meta:
		ordering = ('id',)
		verbose_name = 'Сотрудник'
		verbose_name_plural = 'Сотрудники'


class PersonFilesDocuments(models.Model):
	file_name = models.CharField('Имя файла отображаемое на сайте', max_length=120)
	file = models.FileField(upload_to='team_files', blank=True, null=True, verbose_name='Файл документа')
	attached = models.ForeignKey(Team, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_person_files')

	class Meta:
		ordering = ('id',)
		verbose_name = "Документ сотрудника"
		verbose_name_plural = "Документы сотрудников"

	def __str__(self):
		return self.file_name

