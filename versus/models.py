from django.db import models
from jugador.models import GrupoJugador
# Create your models here.

#tabla num_partidas
class NumSet(models.Model):
	id_num_set = models.AutoField(primary_key=True)
	numero = models.IntegerField(help_text='# set a jugar 1-5')
	distancia = models.IntegerField(help_text='Es variable en exepciones.')

#tabla versus : MANY TO MANY	
class Versus(models.Model):
	id_versus = models.AutoField(primary_key=True)
	id_num_set = models.ForeignKey(NumSet)
	id_grupo_jugador = models.ForeignKey(GrupoJugador)
	
class DetalleVersus(models.Model):
	id_detalle_versus = models.AutoField(primary_key=True)
	id_versus = models.ForeignKey(Versus)
	num_carambola = models.IntegerField()
	# falta mas datos
	