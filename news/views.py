from django.views.generic import ListView, DetailView
import datetime
from .models import Post, Graditude


class PostYears:
	def get_years(self):
		years_sorted_list = Post.objects.filter(draft=False).datetimes('publish', 'year', order='DESC')
		return years_sorted_list


class PostsView(PostYears, ListView):
	"""Список новостей"""
	this_year = datetime.date.today().year
	model = Post
	queryset = Post.objects.filter(draft=False).filter(publish__year=this_year)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['this_year'] = datetime.date.today().year
		return context


class FilterPostsView(PostYears, ListView):
	"""Фильтр по годам публикации"""
	def get_queryset(self):
		return Post.objects.filter(draft=False).filter(publish__year=self.request.GET['year'])

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['this_year'] = self.request.GET['year']
		return context


class PostDetail(DetailView):
	"""Детальное описание новости"""
	model = Post
	slug_field = 'url'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['last_posts'] = Post.objects.filter(draft=False).exclude(url__exact=self.object.url)[:5]
		return context


class GraditudesView(ListView):
	"""Список благодарностей"""
	model = Graditude
	queryset = Graditude.published.filter(status='us')

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['we_graditude'] = Graditude.published.filter(status__exact='we')
		return context


class GraditudeDetail(DetailView):
	model = Graditude
	slug_field = 'url'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['more_grads'] = Graditude.published.filter(status=self.object.status).exclude(url__exact=self.object.url)
		return context
