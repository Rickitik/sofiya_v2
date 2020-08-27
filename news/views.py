from django.views.generic import ListView, DetailView
from .models import Post, Graditude


def get_years_list(model):
	"""Получение списка всех годов публикаций"""
	years_list = []
	raw_object_list = model.objects.filter(draft=False)

	for onedatum in raw_object_list:
		year = onedatum.publish.year
		if year not in years_list:
			years_list.append(year)
	return years_list


class PostsView(ListView):
	"""Список новостей"""
	model = Post
	queryset = Post.objects.filter(draft=False)
	extra_context = {'years_list': get_years_list(model)}


class PostDetail(DetailView):
	"""Детальное описание новости"""
	model = Post
	slug_field = 'url'
	extra_queryset = Post.objects.all()[:5]
	extra_context = {'last_posts': extra_queryset}


class GraditudesView(ListView):
	"""Список благодарностей"""
	model = Graditude
	queryset = Graditude.published.filter(status='us')
	extra_queryset = Graditude.published.filter(status='we')
	extra_context = {'we_graditude': extra_queryset}


class GraditudeDetail(DetailView):
	model = Graditude
	slug_field = 'url'
	extra_queryset = Graditude.published.filter(status='us')[:5]
	extra_context = {'more_graditudes': extra_queryset}
