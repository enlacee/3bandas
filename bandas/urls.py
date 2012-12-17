from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# app nuevo
from nuevo.views import current_datetime,hours_ahead
from torneo.views import add

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bandas.views.home', name='home'),
    # url(r'^bandas/', include('bandas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # --- new  anb ----
    # Mantenimiento Torneo
    url(r'^$','torneo.views.add'),


    # --- applicacion torneo ----    
    url(r'^torneo/$','torneo.views.torneo'),
    # --- applicacion torneo ----    
    #url(r'^torneo/$','torneo.views.torneo'),	
	
	
	
	
    #url(r'^torneo/$','torneo.views.objeto_torneo'),
    url(r'^tiempo/mas/(\d{1,2})/$', 'torneo.views.tiempo_mas'),

    url(r'^torneo/lista/$', 'torneo.views.lista_db'),
    url(r'^torneo/search/$', 'torneo.views.search'),



    # --- web
    url(r'^contacto/$','torneo.views.contacto'),

    # --- applicacion-nuevo ----
    url(r'^nuevo/$',current_datetime), #LLamnado la funcion vista desde  el la app.

    url(r'^nuevo/mas/(\d{1,2})/$',hours_ahead),





    # APP
    # Persona
    url(r'^persona/add/$','persona.views.add'),    

	url(r'^json$','persona.views.json'),   
	













)
