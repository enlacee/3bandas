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
from torneo.models import Pais

# JSON
from django.core.serializers.json import DjangoJSONEncoder

def add(request):
	# Paises
	pais = Pais.objects.all
	tipo_doc = TipoDocumento.objects.all
	departamento = UbigeoDepartamento.objects.all

	data={
	'title':'titulo',
	 'pais':pais,
	 'tipo_doc':tipo_doc,
	 'departamento':departamento
		}		
	return render_to_response('add.html',data,context_instance=RequestContext(request))

def json(request):
	tipo_doc = TipoDocumento.objects.all
	data = {
	'tipo_doc':tipo_doc
	}
	return render_to_response('',tipo_doc)
"""
def view(request):

def edit(request):
"""
