from django.urls import path
from . import views

app_name = 'site_custom'

urlpatterns = [
	path('about', views.about_page, name='about_page'),
	path('program', views.program_page, name='program_page'),
	path('report', views.OtchetView.as_view(), name='report_page'),
	path('report/filter', views.FilterOtchetView.as_view(), name='report_page_filter'),
	path('contacts', views.contact_page, name='contact_page'),
	path('payment', views.payment_page, name='payment_page'),

]
