from django.shortcuts import render
from django.views.generic import CreateView
from .forms import VolunteerForm
from .models import Volunteer
from django.urls import reverse_lazy


class CreateVolunteer(CreateView):
	model = Volunteer
	form_class = VolunteerForm
	template_name = 'volunteer/anketa.html'
	success_url = reverse_lazy('volunteer:volunteer_page_succes')


def suc_page(request):
	return render(request, 'volunteer/succes.html')
