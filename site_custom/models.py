from django.db import models
from .singleton import SingletonModel


class SiteSettings(SingletonModel):
	title = models.CharField(verbose_name='Заголовок сайта главной страницы', max_length=256)
	title_sub_text = models.CharField(verbose_name='Доп. фраза Заголовка главной страницы', max_length=256)
	years_together = models.PositiveSmallIntegerField(verbose_name='Сколько лет работаем', default=0)
	children_count = models.PositiveSmallIntegerField(verbose_name='Сколько детей получило помощь', default=0)
	millions_count = models.PositiveSmallIntegerField(verbose_name='Сколько миллионов собрано', default=0)
	phone_number = models.CharField(verbose_name='Номер телефона в футере и контактах', max_length=256)
	email = models.EmailField(verbose_name='E-mail в футере и контактах')
	address = models.CharField(verbose_name='Почтовый адрес в футере и контактах', max_length=256)
	file_oferta = models.FileField(upload_to='common_files', blank=True, null=True, verbose_name='Документ оферты')
	file_schema_proezda = models.FileField(upload_to='common_files', blank=True, null=True, verbose_name='Схема проезда')
	rekv_name = models.CharField(verbose_name='Реквизиты - Наименование фонда', max_length=256)
	rekv_address = models.CharField(verbose_name='Реквизиты - Адрес', max_length=256)
	rekv_INN = models.CharField(verbose_name='Реквизиты - ИНН', max_length=100)
	rekv_KPP = models.CharField(verbose_name='Реквизиты - КПП', max_length=100)
	rekv_rasch_schet = models.CharField(verbose_name='Реквизиты - р.счет', max_length=50)
	rekv_bank_name = models.CharField(verbose_name='Реквизиты - Наименование банка', max_length=200)
	rekv_k_schet = models.CharField(verbose_name='Реквизиты - к.счет', max_length=50)
	rekv_bik = models.CharField(verbose_name='Реквизиты - БИК', max_length=50)
	file_rekvizity = models.FileField(upload_to='common_files', blank=True, null=True,
										   verbose_name='Файл реквизиты')
	file_pers_data = models.FileField(upload_to='common_files', blank=True, null=True, verbose_name='Файл обработка персональных данных')
	file_zayavleniye = models.FileField(upload_to='common_files', blank=True, null=True, verbose_name='Файл Заявление на получение помощи')
	file_list_documents = models.FileField(upload_to='common_files', blank=True, null=True, verbose_name='Файл Перечень документов')

	def __str__(self):
		return 'Настройки'

	class Meta:
		verbose_name = "Основные настройки сайта"
		verbose_name_plural = "Основные настройки сайта"


class ProgramFilesDocuments(models.Model):
	file_name = models.CharField('Имя файла отображаемое на сайте', max_length=120)
	file = models.FileField(upload_to='program_files', blank=True, null=True, verbose_name='Файл документа')
	attached = models.ForeignKey(SiteSettings, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_program_files')

	class Meta:
		ordering = ('id',)
		verbose_name = "Документ 'Программа Здоровье'"
		verbose_name_plural = "Документы 'Программа Здоровье'"

	def __str__(self):
		return self.file_name


class ProgramFilesGallery(models.Model):
	file = models.FileField(upload_to='program_gallery', blank=True, null=True, verbose_name='Файл Галереи')
	attached = models.ForeignKey(SiteSettings, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_program_photos')

	class Meta:
		verbose_name = "Слайд галереи 'Программа Здоровье'"
		verbose_name_plural = "Слайды галереи 'Программа Здоровье'"

	def __str__(self):
		return self.file.name


class AboutFilesDocuments(models.Model):
	file_name = models.CharField('Имя файла отображаемое на сайте', max_length=120)
	file = models.FileField(upload_to='about_files', blank=True, null=True, verbose_name='Файл документа')
	attached = models.ForeignKey(SiteSettings, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_about_files')

	class Meta:
		ordering = ('id',)
		verbose_name = "Уставные Документы"
		verbose_name_plural = "Уставные Документы"

	def __str__(self):
		return self.file_name


class AboutFilesGallery(models.Model):
	file = models.FileField(upload_to='about_gallery', blank=True, null=True, verbose_name='Файл Галереи')
	attached = models.ForeignKey(SiteSettings, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_photos')

	class Meta:
		verbose_name = "Слайд галереи 'О нас'"
		verbose_name_plural = "Слайды галереи 'О нас'"

	def __str__(self):
		return self.file.name


class ReportFilesDocuments(models.Model):
	file_name = models.CharField('Имя файла отображаемое на сайте', max_length=120)
	file_date = models.DateField('Месяц отчета')
	file = models.FileField(upload_to='report_files', blank=True, null=True, verbose_name='Файл документа')
	attached = models.ForeignKey(SiteSettings, blank=True, null=True, on_delete=models.CASCADE, related_name='attached_report_files')

	class Meta:
		ordering = ('file_date',)
		verbose_name = "Месячный Отчет"
		verbose_name_plural = "Месячные Отчеты"

	def __str__(self):
		return f'{self.file_name}-{self.file_date}'
