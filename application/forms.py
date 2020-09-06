from .models import Application
from django.forms import ModelForm, TextInput, Textarea, FileField
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class ApplicationForm(ModelForm):
	"""Форма заявки"""
	captcha = ReCaptchaField()

	class Meta:
		model = Application
		exclude = ['request_date']
		labels = {'problem': ''}
		widgets = {
			'fio': TextInput(attrs={'placeholder': 'Иванов Иван Иванович'}),
			'problem': Textarea(attrs={'placeholder': 'Краткое изложение проблемы и степень срочности ее решения*',
									'cols': '50',
									'rows': '10'}),
		}
