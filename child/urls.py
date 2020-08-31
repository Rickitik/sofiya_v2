from django.urls import path
from . import views

app_name = 'child'

urlpatterns = [
	path('children/', views.ChildrenView.as_view(), name='child_list'),
	path('children/<slug:slug>', views.ChildDetail.as_view(), name='child_detail'),
	path('', views.home_page, name='home_page'),
]
