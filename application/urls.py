# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = 'application'

urlpatterns = [
	path('', views.CreateApplication.as_view(), name='application_page'),
	path('success', views.suc_page, name='app_page_succes'),
	# TODO: страница успеха настроить
	# TODO: стили для ошибок в форме
]
