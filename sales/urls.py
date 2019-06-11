from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
	url(r'^$', views.index, name='sale_index'),
	url(r'^new$', views.create, name='sale_index'),
	#url(r'^(?P<id>\d+)/view$', views.index, name='sale_index'),
	#url(r'^(?P<id>\d+)/show$', views.index, name='sale_index'),
	#url(r'^(?P<id>\d+)/edit$', views.index, name='sale_index'),
]