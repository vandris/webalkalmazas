from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.adds, name='adds'),
	url(r'^admin/', admin.site.urls),
	]