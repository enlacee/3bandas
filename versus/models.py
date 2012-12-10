from django.db import models
from jugador.models import GrupoJugador
# Create your models here.

#tabla num_partidas
class NumPartida(models.Model):
	id_num_partida = models.AutoField(primary_key=True)
	numero = models.IntegerField(help_text='# de batalla defaul 1 para todos [1-10]')

#tabla versus : MANY TO MANY	
class Versus(models.Model):
	id_versus = models.AutoField(primary_key=True)
	id_num_partida = models.ForeignKey(NumPartida)
	id_grupo_jugador = models.ForeignKey(GrupoJugador)
	
class DetalleVersus(models.Model):
	id_detalle_versus = models.AutoField(primary_key=True)
	id_versus = models.ForeignKey(Versus)
	num_carambola = models.IntegerField()
	# falta mas datos
	