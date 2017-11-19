from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.conf.urls.static import static
from django.conf import settings

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
	url(r'^search_owner/$', views.search_owner, name='search_owner'),
	url(r'^delete_add/$', views.delete_add, name='delete_add'),
	url(r'^users/', views.users, name='users'),
	url(r'^delete_user/$', views.delete_user, name='delete_user'),
	url(r'^modify/$', views.modify, name='modify'),
	url(r'^modify_add/$', views.modify_add, name='modify_add'),

	#url(r'^$', views.index, name='index'),
	url(r'^(?P<id>[0-9]+)/$', views.adds, name='adds'),
	url(r'^admin/', admin.site.urls),
	] \

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)