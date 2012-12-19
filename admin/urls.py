from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from admin.views import add


#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
	#url(r'^$','torneo.views.add'),
    url(r'^adm/add/$','admin.views.add'),    

     


)
