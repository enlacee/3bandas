from django.db import models
#importanto modelo PERSONA
from persona.models import Persona
from torneo.models import Torneo
from torneo.models import Grupo

# tabla = categorias_juegos
class CategoriaJuego(models.Model):
	id_categoria_juego = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30,help_text='A los jugadores se le clasifica por Categoria')
	def __unicode__(self):
		return self.descripcion
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
