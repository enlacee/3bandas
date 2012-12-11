from django.db import models
#importanto modelo PERSONA
from torneo.models import Torneo,Grupo
from persona.models import Persona
from torneo.models import CategoriaJuego
#from torneo.models import Torneo,Grupo,Handicap



# tabla = jugadores
class Jugador(models.Model):
	id_jugador = models.AutoField(primary_key=True) 
	id_persona = models.ForeignKey(Persona,unique=True,editable=False)
	id_categoria_juego = models.ForeignKey(CategoriaJuego)
	def __unicode__(self):
		return self.id_jugador



#tabla torneos_jugadores : MANY TO MANY
class TorneoJugador(models.Model):
	id_torneo_jugador = models.AutoField(primary_key=True)
	id_torneo = models.ForeignKey(Torneo)
	id_jugador = models.ForeignKey(Jugador)
	fecha_creacion = models.DateField(auto_now=True)
			
#tabla grupos_jugadores : MANY TO MANY		
class GrupoJugador(models.Model):
	id_grupo_jugador = models.AutoField(primary_key=True)
	id_torneo_jugador= models.ForeignKey(TorneoJugador)
	id_grupo = models.ForeignKey(Grupo)
