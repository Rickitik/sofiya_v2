from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ApplicationForm
from .models import Application
from django.urls import reverse_lazy


class CreateApplication(CreateView):
	model = Application
	form_class = ApplicationForm
	template_name = 'application/help_request.html'
	success_url = reverse_lazy('application:app_page_succes')


def suc_page(request):
	return render(request, 'application/success_app.html')
