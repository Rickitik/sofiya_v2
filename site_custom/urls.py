from django.urls import path
from . import views

app_name = 'site_custom'

urlpatterns = [
	path('about', views.about_page, name='about_page'),
	path('program', views.program_page, name='program_page'),
	path('report', views.otchet_page, name='report_page'),
	path('contacts', views.contact_page, name='contact_page'),

]
