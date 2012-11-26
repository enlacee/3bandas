# Create your views here.
from torneo.models import Torneo
from torneo.models import Pais
from django.shortcuts import render_to_response

import datetime

def lista_torneos(request):
	torneos = Torneo.objects.all()
	anibal = 'anb copitan'
	#return render_to_response('lista_torneos.html', {'lista':torneos}, context_instance=RequestContext(request))
	return render_to_response('lista_torneos.html', {'lista':torneos,'anibal':anibal})

def objeto_torneo(request):
	data = ['uno','dos','tres','cuatro']
	ide = 'anb'
	nombre = 'Anibal Copitan Norabuena'
	tiempo = datetime.datetime.now()
	fuck = '<< direccionales  >> ok //'

	diccionario = {'data':data,'ide':ide,'nombre':nombre,'tiempo':tiempo,'fuck':fuck}
	return render_to_response('torneo.html', diccionario )
	#return render_to_response('public/demo.html', diccionario )

