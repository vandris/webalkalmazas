from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^search/', views.search, name='search'),
	url(r'^login/', views.login, name='login'),
	url(r'^signup/',views.signup, name='signup'),
	url(r'^change_password/', views.change_password, name='change_password'),
	url(r'^addadd/', views.addadd, name='addadd'),
	url(r'^created/$', views.addHouse, name='addHouse'),
	url(r'^searchresults/$', views.searchHouse, name='searchHouse'),
	url(r'^connect/$', views.contact, name='contact'),
	url(r'^messages/', views.messages, name='messages'),
	url(r'^send_messages/$', views.send_messages, name='send_messages'),
	url(r'^send_newmessages/$', views.send_newmessages, name='send_newmessages'),

	#url(r'^$', views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.adds, name='adds'),
	url(r'^admin/', admin.site.urls),
	]