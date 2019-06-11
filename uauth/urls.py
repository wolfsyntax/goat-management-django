from django.conf.urls import url
from django.views.generic import TemplateView

## User defined
from . import views
urlpatterns = [
	url(r'^login$', views.index, name="login"),
	url(r'^join$', views.register, name='signup'),
	url(r'^logout$', views.destroy, name='logout')
]