from django.core.validators import FileExtensionValidator
from django.db import models


class Application(models.Model):
	fio = models.CharField('ФИО отправителя*', max_length=50)
	photo = models.ImageField('Фотография ребенка*', upload_to='apps/%Y/%m/%d/')
	signature = models.FileField('Скан заявления с подписью (PDF)*', upload_to='apps/%Y/%m/%d/', validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	problem = models.TextField()
	file1 = models.FileField('Документ 1 (PDF)', upload_to='apps/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	file2 = models.FileField('Документ 2 (PDF)', upload_to='apps/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	file3 = models.FileField('Документ 3 (PDF)', upload_to='apps/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	file4 = models.FileField('Документ 4 (PDF)', upload_to='apps/%Y/%m/%d/', blank=True, null=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
	request_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.fio

	class Meta:
		ordering = ('-id',)
		verbose_name = 'Заявка'
		verbose_name_plural = 'Заявки'

