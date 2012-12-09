# Create your views here.
from torneo.models import Torneo
from torneo.models import Pais
from django.db.models import Q
from django.shortcuts import render_to_response

#libreria formulario
#from django.forms import ContactForm
#from torneo.models import Torneo
from django.http import HttpResponse, HttpResponseRedirect
from torneo.forms import ContactForm, TorneoForm
from django.core.mail import send_mail

from django.template import RequestContext


import MySQLdb
import datetime

def torneo(request):
	return render_to_response('torneo.html')

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



"""
#Pagina Contacto
def contacto(request):
	#form = ContactForm()
	#return render_to_Response('public/contacto.html',{'form':form})
if request.method == 'POST':
		formulario = ContactForm()
		if(formulario.is_valid()):
			titulo = 'Mensaje desde el Toreno'
			contenido = formulario.cleaned_data['mensaje'] + "\n"
			contenido += 'Cominiquese a :' + formulario.cleaned_data['correo']
			correo  = EmailMessage(titulo, contenido,to=['destinatario@gmail.com'])
			correo.send()
			#return HttoResponseRedirect('/')
		else:
			formulario = ContactForm()

	#formulario = TorneoForm()#ContactForm()
	data = {'nombre': u'John', 'correo': u'anb','mensaje':u'vacio'}			
	#formulario = ContactForm(data,auto_id='id_for_%s', label_suffix='')
	formulario = ContactForm(data)
	formulario['nombre'].css_classes('anibal copitan')
	formulario['mensaje'].css_classes('foo bar')
	if True:#formulario.is_valid():
		return render_to_response('public/contacto.html',{'formulario':formulario})
"""

def contact(request):
	if request.method == 'GET':
		formulario = ContactForm(request.GET)		
		if formulario.is_valid():						
			#nombre = formulario.clean_data['nombre']
			#mensaje = formulario.clean_data['mensaje']
			return render_to_response('public/contacto.html',{'formulario':formulario})
	else:
		formulario = ContactForm()
	return render_to_response('public/contacto.html',{'formulario':formulario})

def contacto(request):
    if request.method=='POST':    	
        formulario = ContactForm(request.POST)
        if formulario.is_valid():
            return HttpResponseRedirect('/correcto')
    else:
        formulario = ContactForm()
    return render_to_response('public/contacto.html',{'formulario':formulario}, context_instance=RequestContext(request))
