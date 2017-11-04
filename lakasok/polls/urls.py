from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^search/', views.search, name='search'),
	url(r'^login/', views.login, name='login'),
	url(r'^addadd/', views.addadd, name='addadd'),
	url(r'^felvesz/$', views.addHouse, name='addHouse'),

	#url(r'^$', views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.adds, name='adds'),
	url(r'^admin/', admin.site.urls),
	]