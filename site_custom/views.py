from django.shortcuts import render
from .models import SiteSettings, AboutFilesDocuments, AboutFilesGallery, ProgramFilesDocuments, ProgramFilesGallery, ReportFilesDocuments


def get_years_list(model):
	"""Получение списка всех годов публикаций"""
	years_list = []
	raw_object_list = model.objects.all()

	for onedatum in raw_object_list:
		year = onedatum.file_date.year
		if year not in years_list:
			years_list.append(year)
	return years_list


def about_page(request):
	context = {}
	context['docs'] = AboutFilesDocuments.objects.all()
	context['slides'] = AboutFilesGallery.objects.all()
	return render(request, 'site/about.html', context=context)


def program_page(request):
	context = {}
	context['docs']= ProgramFilesDocuments.objects.all()
	context['slides'] = ProgramFilesGallery.objects.all()
	return render(request, 'site/program.html', context=context)


def otchet_page(request):
	context = {}
	context['years'] = get_years_list(ReportFilesDocuments)
	context['docs'] = ReportFilesDocuments.objects.all()
	return render(request, 'site/report.html', context=context)


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
