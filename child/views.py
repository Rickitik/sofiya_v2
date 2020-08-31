from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Child


class ChildrenView(ListView):
	"""Списки детей"""
	model = Child
	queryset = Child.published.filter(status='need_help')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['already_helped'] = Child.published.filter(status='already_help')
		return context


class ChildDetail(DetailView):
	"""Информация о ребенке"""
	model = Child
	slug_field = 'url'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['also_need_help'] = Child.published.filter(status='need_help').exclude(url__exact=self.object.url)
		return context


def home_page(request):
	context = {}
	context['need_help_children'] = Child.published.filter(status='need_help')
	context['already_helped_children'] = Child.published.filter(status='already_help')
	return render(request, 'child/home.html', context=context)
