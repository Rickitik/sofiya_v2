from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager, self).get_queryset().filter(draft=False)


class Post(models.Model):
	title = models.CharField('Заголовок новости', max_length=250)
	url = models.SlugField(max_length=250, unique=True)
	body = models.TextField('Основной контент новости')
	publish = models.DateTimeField('Дата публикации', default=timezone.now)
	photo = models.ImageField('Изображение', upload_to='news_images')
	draft = models.BooleanField('Черновик', default=True)

	def __str__(self):
		return self.title

	def was_published_recently(self):
		return self.publish >= timezone.now() - datetime.timedelta(days=100)

	def get_absolute_url(self):
		return reverse('news:post_detail', kwargs={'slug': self.url})

	class Meta:
		ordering = ('-publish',)
		verbose_name = 'Новость'
		verbose_name_plural = 'Новости'


class Graditude(models.Model):
	title = models.CharField('Кто благодарит/кого благодарим мы', max_length=250)
	url = models.SlugField(max_length=250, unique=True)
	publish = models.DateTimeField('Дата публикации')
	photo = models.ImageField('Изображение', upload_to='gratitude_images')
	draft = models.BooleanField('Черновик', default=True)
	STATUS_CHOICES = (
		('we', 'Мы благодарим'),
		('us', 'Нас благодарят'),
	)
	status = models.CharField('Кто благодарит', max_length=18, choices=STATUS_CHOICES, default='us')
	objects = models.Manager()  # The default manager.
	published = PublishedManager()  # Our custom manager.

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('news:graditude_detail', kwargs={'slug': self.url})

	class Meta:
		ordering = ('-publish',)
		verbose_name = 'Благодарность'
		verbose_name_plural = 'Благодарности'
