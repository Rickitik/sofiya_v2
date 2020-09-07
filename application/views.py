from django.shortcuts import render
from django.views.generic import CreateView
from .forms import ApplicationForm
from .models import Application
from django.urls import reverse_lazy
from django.core.mail import send_mail


class CreateApplication(CreateView):
	model = Application
	form_class = ApplicationForm
	template_name = 'application/help_request.html'
	success_url = reverse_lazy('application:app_page_succes')

	def form_valid(self, form):
		"""If the form is valid, save the associated model."""
		# send_mail('Some title', 'Body text', 'my@mail.com', ['11@mail.com'])
		self.object = form.save()
		return super().form_valid(form)


def suc_page(request):
	return render(request, 'application/success_app.html')
