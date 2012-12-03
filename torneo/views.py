# Create your views here.
from torneo.models import Torneo
from torneo.models import Pais
from django.db.models import Q
from django.shortcuts import render_to_response
#
#from torneo.models import Torneo

from forms import ContactForm


import MySQLdb
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


def tiempo_mas(request, offset):
	offset = int(offset)	
	title = 'titulo de plantilla con herencia ANB'
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)	
	return render_to_response('public/index.html',{'title':title, 'offset':offset, 'dt':dt})

"""
def lista_db(request):
	db = MySQLdb.connect(user='root', db='bandas',passwd='', host='localhost')
	cursor = db.cursor()
	cursor.execute('select *from torneo_pais')	
	names = [row[0] for row in  cursor.fetchall()]
	db.close()
	return render_to_response('public/torneo.html',{'names':names})

"""
def lista_db(request):
	torneo = Torneo.objects.order_by('nombre')
	return render_to_response('public/torneo.html',{'torneo' : torneo})

def search(request):
	query = request.GET.get('q','');
	if query:
		qset =(
			Q(nombre__icontains=query)|
			Q(descripcion__icontains=query)
			#Q(descripcion__icontains=query)|
		)
		results = Torneo.objects.filter(qset).distinct()
	else:
		results = []
	return render_to_response('public/search.html',{
		'results' : results,
		'query' : query
	})


#Pagina Contacto
def contact(request):
	form = ContactForm()
	return render_to_Response('public/contacto.html',{'form':form})