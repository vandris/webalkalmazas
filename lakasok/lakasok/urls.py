from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth import login

urlpatterns = [
    # Examples:
    # url(r'^$', 'lakasok.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^polls/', include('polls.urls')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
]
