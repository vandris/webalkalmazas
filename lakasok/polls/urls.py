from django.conf.urls import url
from . import views
from django.contrib import admin

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^search/', views.search, name='search'),
	url(r'^login/', views.login, name='login'),
	url(r'^signup/',views.signup, name='signup'),
	url(r'^addadd/', views.addadd, name='addadd'),
	url(r'^created/$', views.addHouse, name='addHouse'),
	url(r'^searchresults/$', views.searchHouse, name='searchHouse'),
	url(r'^connect/$', views.contact, name='contact'),

	#url(r'^$', views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.adds, name='adds'),
	url(r'^admin/', admin.site.urls),
	]