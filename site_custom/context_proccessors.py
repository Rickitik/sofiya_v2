# -*- coding: utf-8 -*-

from .models import SiteSettings


def load_settings(request):
	return {'site_settings': SiteSettings.load()}
