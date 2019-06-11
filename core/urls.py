from django.conf.urls import url
from django.views.generic import TemplateView

## User defined
from . import views
urlpatterns = [
	url(r'^$', views.manage, name="manage_goat"),
	url(r'^new/$', views.index, name="new_goat"),
	url(r'^(?P<tag_id>\d+)/edit$', views.edit_goat, name="edit_goat"),
	url(r'^(?P<tag_id>\d+)/show$', views.view_goat, name="view_goat"),
]