from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Team


class TeamList(ListView):
	"""Списки сотрудников"""
	model = Team


class TeamDetail(DetailView):
	"""Данные сотрудника"""
	model = Team
	slug_field = 'url'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['other_persons'] = Team.objects.all().exclude(url__exact=self.object.url)
		return context
