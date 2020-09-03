from django.db import models


class Volunteer(models.Model):
	PRACTICE_CHOICES = (
		('y', 'Да'),
		('n', 'Нет'),
	)
	name = models.CharField('Имя*', max_length=20)
	phone = models.CharField('Телефон*', max_length=15)
	email = models.EmailField('E-mail*', max_length=50)
	practice = models.CharField('Волонтерский опыт — да/нет', max_length=10, choices=PRACTICE_CHOICES, default='n')
	Age = models.PositiveSmallIntegerField('Возраст', blank=True, null=True)
	graduation = models.CharField('Образование', max_length=20, blank=True, null=True)
	job = models.CharField('Род деятельности в настоящее время', max_length=50, blank=True, null=True)
	social = models.CharField('Aккаунт в соцсети (Fb/Vk/Inst)', max_length=50, blank=True, null=True)
	photo = models.ImageField('Фотография*', upload_to='volunteer/%Y/%m/%d/')
	about = models.TextField('Расскажите о себе*')
	sent = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('sent',)
		verbose_name = 'Волонтер'
		verbose_name_plural = 'Волонтеры'

