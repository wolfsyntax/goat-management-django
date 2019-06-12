from django.conf.urls import url
from django.views.generic import TemplateView

## User defined
from . import views
urlpatterns = [
	url(r'^$', views.index, name="home_page"),
	url(r'^about/$', views.about, name='about_page'),
	url(r'^contact$', views.contact, name='contact_page'),
	url(r'^faq$', views.faq, name='support_page'),
	url(r'^dashboard$', views.dashboard, name="main_page"),
]