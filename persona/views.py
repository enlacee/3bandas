#encoding:utf-8
from persona.models import Persona,TipoDocumento,UbigeoDepartamento
from jugador.models import Jugador

# Plantilla
from django.template import RequestContext
# HTTP
from django.http import HttpResponse, HttpResponseRedirect
# Libreria Abreviado
from django.shortcuts import render_to_response
# Formulario Persona
from persona.forms import FormPersona

# Data
from torneo.models import Pais,Estados

# data JSON
from django.utils import simplejson
# Serializar Datos
from django.core import serializers 

def add(request):
	# Paises
	pais = Pais.objects.all
	tipo_doc = TipoDocumento.objects.all
	departamento = UbigeoDepartamento.objects.all

	data={
	'title':'Persona',
	 'pais':pais,
	 'tipo_doc':tipo_doc,
	 'departamento':departamento
		}		
	return render_to_response('add.html',data,context_instance=RequestContext(request))

"""
def view(request):

def edit(request):
"""

def json_pais(request):
	# Paises		 
   	data = serializers.serialize("json", Pais.objects.all())
   	return 	HttpResponse(simplejson.dumps(data), mimetype='application/json')

def json_estados(request,id):	
   	data = serializers.serialize("json", Estados.objects.filter(id_pais_id=id))
   	return 	HttpResponse(simplejson.dumps(data), mimetype='application/json')