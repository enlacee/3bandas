#encoding:utf-8
# Plantilla
from django.template import RequestContext
# HTTP
from django.http import HttpResponse, HttpResponseRedirect
# Libreria Abreviado
from django.shortcuts import render_to_response

def add(request):		
	data={
	'title':'Administrador',	
	}
	# Error cuando tengo 2 aplicaciones 
	return render_to_response('add_admin.html',data,context_instance=RequestContext(request))