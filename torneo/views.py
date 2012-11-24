# Create your views here.
from torneo.models import Torneo
from torneo.models import Pais
from django.shortcuts import render_to_response

def lista_torneos(request):
	torneos = Torneo.objects.all()
	anibal = 'anb copitan'
	#return render_to_response('lista_torneos.html', {'lista':torneos}, context_instance=RequestContext(request))
	return render_to_response('lista_torneos.html', {'lista':torneos,'anibal':anibal})