"""adnusp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#default
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, handler404, handler500, handler403
#additional
#from django.conf.urls import url
#from django.conf.urls import url, handler405, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include(('sitemap.urls','sitemap')), name='sitemap'),
    url(r'^auth/', include(('uauth.urls','uauth')), name='uauth'),
    url(r'^goat/', include(('core.urls','core')), name='core'),
    url(r'^sales/', include(('sales.urls','sales')), name='sales'),
]

handler404='sitemap.views.custom404'
handler500='sitemap.views.custom500'
handler403='sitemap.views.custom403'