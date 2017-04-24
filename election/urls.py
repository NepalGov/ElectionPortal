"""election URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from e2074.views import *
from django.contrib.auth.views import login,logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^wp-admin/login/$', login, name='login'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^wp-admin/logout/$', logout, {'next_page':'home'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^wp-admin/$', wpadmin, name='wpadmin'),
    url(r'^wp-admin/zone/$', wpzone, name='wpzone'),
    url(r'^wp-admin/district/$', wpdistrict, name='wpdistrict'),
    url(r'^wp-admin/politicaldiv/$', wppoliticaldiv, name='wppoliticaldiv'),
    url(r'^wp-admin/candidate/$', wpcandidate, name='wpcandidate'),
    url(r'^parties/$', parties, name='parties'),
    url(r'^getinvolved/$', getinvolved, name='getinvolved'),
    url(r'^candidates/$', candidates, name='candidates'),
    url(r'^parties/(?P<slug>[\w-]+)/$', partyprofile, name='partyprofile'),
    url(r'^explore/$', explore, name='explore'),
    url(r'^explore/(?P<name>[\w-]+)/$', district, name='district'),
    url(r'^explore/(?P<name>[\w-]+)/(?P<name2>[\w-]+)/$', politicaldiv, name='politicaldiv'),
    url(r'^(?P<slug>[\w-]+)/$', post, name='post'),
    url(r'^(?P<district>[\w-]+)/(?P<politicaldiv>[\w-]+)/(?P<slug>[\w-]+)/$', profile, name='profile'),
    url(r'^suggest/district/$', suggestdistrict, name="suggestdistrict"),
    url(r'^suggest/politicaldiv/$', suggestpoliticaldiv, name="suggestpoliticaldiv"),


]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
