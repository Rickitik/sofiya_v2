from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('news/', views.PostsView.as_view(), name='post_list'),
    path('news/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),
    path('graditudes/', views.GraditudesView.as_view(), name='grad_list'),
    path('graditudes/<slug:slug>', views.GraditudeDetail.as_view(), name='grad_detail'),
]
