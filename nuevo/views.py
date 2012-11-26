# Importando la clase HttpResponse del modulo django.http
from django.http import HttpResponse
# Importando datetime de biblioteca de python
import datetime

# Funcion de vista toma como primer parametro al objeto HttpResponse 
def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>Hora actual es %s.</body></htm l>" % now
	return HttpResponse(html)


def hours_ahead(request, offset):
	offset = int(offset)	
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)