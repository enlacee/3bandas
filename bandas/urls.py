from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

# app nuevo
from nuevo.views import current_datetime,hours_ahead

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
    url(r'^$','torneo.views.lista_torneos'),

    # --- applicacion torneo ----
    url(r'^torneo/$','torneo.views.objeto_torneo'),
    url(r'^tiempo/mas/(\d{1,2})/$', 'torneo.views.tiempo_mas'),

    # --- applicacion-nuevo ----
    url(r'^nuevo/$',current_datetime), #LLamnado la funcion vista desde  el la app.

    url(r'^nuevo/mas/(\d{1,2})/$',hours_ahead),
)
