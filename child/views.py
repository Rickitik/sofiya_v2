from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Child


class ChildrenView(ListView):
	"""Списки детей"""
	model = Child
	queryset = Child.published.filter(status='need_help')
	extra_queryset = Child.published.filter(status='already_help')
	extra_context = {'already_helped': extra_queryset}


class ChildDetail(DetailView):
	"""Информация о ребенке"""
	model = Child
	slug_field = 'url'
	extra_queryset = Child.published.filter(status='need_help')
	extra_context = {'also_need_help': extra_queryset}
