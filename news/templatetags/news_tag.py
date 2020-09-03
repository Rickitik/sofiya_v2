# -*- coding: utf-8 -*-
from django import template
from news.models import Post

register = template.Library()


@register.simple_tag()
def get_news(count=5):
	return Post.objects.all()[:count]

