from .models import Volunteer
from django.forms import ModelForm, TextInput, Textarea
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class VolunteerForm(ModelForm):
	"""Форма заявки"""
	captcha = ReCaptchaField()
	class Meta:
		model = Volunteer
		exclude = ['sent']
		labels = {'about': ''}
		widgets = {
			'name': TextInput(attrs={'placeholder': 'Сергей'}),
			'phone': TextInput(attrs={'placeholder': '+7-916-299-99-99'}),
			'email': TextInput(attrs={'placeholder': 'puff@yandex.ru'}),
			'Age': TextInput(attrs={'placeholder': '18'}),
			'graduation': TextInput(attrs={'placeholder': 'Среднее'}),
			'job': TextInput(attrs={'placeholder': 'студент'}),
			'social': TextInput(attrs={'placeholder': '@puff'}),
			'about': Textarea(attrs={'placeholder': 'Расскажите о себе*', 'cols': '53', 'rows': '10'}),
		}
