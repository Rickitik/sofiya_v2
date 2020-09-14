from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(publicated_on_site=True)


class Child(models.Model):
	"""Данные ребенка"""
	STATUS_CHOICES = (
		('need_help', 'Нуждается в помощи'),
		('already_help', 'Помогли'),
	)
	name = models.CharField('Имя', max_length=12)
	name_rod = models.CharField('Имя в родительном падеже', max_length=15)  # История Саши....
	surname = models.CharField('Фамилия', max_length=20)
	lastname = models.CharField('Отчество', max_length=20)
	birthday = models.DateField('Дата рождения')
	age = models.CharField('Возраст ребенка', max_length=15, help_text='2 годика / 3 года / 5 лет ...')
	place = models.CharField('Город проживания', max_length=20, help_text='г. Москва')
	problem = models.TextField('Проблема ребенка')  # Краткое пояснение проблемы
	history = models.TextField('История ребенка')  # История ребенка
	photo = models.ImageField('Изображение', upload_to='child_photo')  # 540Х400px оптимальный размер
	url = models.SlugField(max_length=130, unique=True)
	money_need = models.PositiveIntegerField('Необходимая сумма в рублях')
	money_collected = models.PositiveIntegerField('Собранная сумма в рублях', default=0)
	status = models.CharField('Статус ребенка', max_length=15, choices=STATUS_CHOICES, default='need_help')
	problem_solution = models.CharField('Решение проблемы', max_length=60, blank=True, null=True)
	publicated_on_site = models.BooleanField('Опубликована анкета', default=False)  # Опубликована ли анкета
	objects = models.Manager()  # The default manager.
	published = PublishedManager()  # Our custom manager.

	def __str__(self):
		return f'{self.surname} {self.name}'

	def get_absolute_url(self):
		return reverse('child:child_detail', kwargs={'slug': self.url})

	def left_amount_money(self):
		return self.money_need - self.money_collected

	class Meta:
		verbose_name = 'Ребенок'
		verbose_name_plural = 'Дети'
