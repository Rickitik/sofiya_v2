import datetime
from django.shortcuts import render
from django.views.generic import ListView
from .models import SiteSettings, AboutFilesDocuments, AboutFilesGallery, ProgramFilesDocuments, ProgramFilesGallery, \
	ReportFilesDocuments, YearReportFilesDocuments


def about_page(request):
	context = {}
	context['docs'] = AboutFilesDocuments.objects.all()
	context['slides'] = AboutFilesGallery.objects.all()
	return render(request, 'site/about.html', context=context)


def program_page(request):
	context = {}
	context['docs'] = ProgramFilesDocuments.objects.all()
	context['slides'] = ProgramFilesGallery.objects.all()
	return render(request, 'site/program.html', context=context)


class ReportYears:
	def get_years(self):
		years_sorted_list = YearReportFilesDocuments.objects.all().dates('file_date', 'year', order='DESC')
		return years_sorted_list


class OtchetView(ReportYears, ListView):
	"""Отчеты"""
	this_year = datetime.date.today().year
	model = ReportFilesDocuments
	queryset = ReportFilesDocuments.objects.filter(file_date__year=this_year)
	template_name = 'site/report.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['year_reports'] = YearReportFilesDocuments.objects.filter(file_date__year=datetime.date.today().year)
		context['this_year'] = datetime.date.today().year
		return context


class FilterOtchetView(ReportYears, ListView):
	"""Фильтр по годам публикации"""
	template_name = 'site/report.html'

	def get_queryset(self):
		return ReportFilesDocuments.objects.filter(file_date__year=self.request.GET['year'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['year_reports'] = YearReportFilesDocuments.objects.filter(file_date__year=self.request.GET['year'])
		context['this_year'] = self.request.GET['year']
		return context


def contact_page(request):
	context = {}
	obj = SiteSettings.objects.get()
	context['address'] = obj.rekv_address
	context['schema'] = obj.file_schema_proezda
	context['mail'] = obj.email
	context['phone'] = obj.phone_number
	context['file_rekv'] = obj.file_rekvizity
	context['name'] = obj.rekv_name
	context['inn'] = obj.rekv_INN
	context['kpp'] = obj.rekv_KPP
	context['ras_schet'] = obj.rekv_rasch_schet
	context['bank'] = obj.rekv_bank_name
	context['kor_schet'] = obj.rekv_k_schet
	context['bik'] = obj.rekv_bik

	return render(request, 'site/contacts_page.html', context=context)


def payment_page(request):
	context = {}
	obj = SiteSettings.objects.get()
	context['address'] = obj.rekv_address
	context['file_rekv'] = obj.file_rekvizity
	context['file_blank'] = obj.file_forma_forbank
	context['name'] = obj.rekv_name
	context['inn'] = obj.rekv_INN
	context['kpp'] = obj.rekv_KPP
	context['ras_schet'] = obj.rekv_rasch_schet
	context['bank'] = obj.rekv_bank_name
	context['kor_schet'] = obj.rekv_k_schet
	context['bik'] = obj.rekv_bik

	return render(request, 'site/payment.html', context=context)
