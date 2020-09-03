from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
	path('<slug:slug>', views.TeamDetail.as_view(), name='team_detail'),
	path('', views.TeamList.as_view(), name='team_list'),
]
