from django.urls import path
from . import views

app_name = 'volunteer'

urlpatterns = [
	path('anketa', views.CreateVolunteer.as_view(), name='volunteer_page_form'),
	path('success', views.suc_page, name='volunteer_page_succes'),
]
