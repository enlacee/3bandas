from django.db import models
#from jugador.models import CategoriaJuego
#import Jugador,CategoriaJuego

# tabla estados		
class Estados(models.Model):
	id_estado = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30)	
	def __str__(self):
		return self.descripcion	


# tabla paises
class Pais(models.Model):
	id_pais = models.AutoField(primary_key=True) 
	id_estado = models.ForeignKey(Estados)
	descripcion = models.CharField(max_length=30)
	descripcion_corta = models.CharField(max_length=4,default=True)
	def __str__(self):
		return self.descripcion
		
	
		
# tabla = categorias_juegos
class CategoriaJuego(models.Model):
	id_categoria_juego = models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30,help_text='A los jugadores se le clasifica por Categoria')
	def __unicode__(self):
		return self.descripcion		
		
# tabla torneos
class Torneo(models.Model):
	id_torneo = models.AutoField(primary_key=True)
	id_pais = models.ForeignKey(Pais)
	id_estado = models.ForeignKey(Estados)
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField()	
	handicap_estado = models.BooleanField()
	numero_mesas = models.IntegerField()	
	numero_jugadores = models.IntegerField(help_text='Numero de Jugadores para empezar partida')
	param_puntos = models.BooleanField(default=True,editable=False,help_text='Parametro de clasificacion 1')
	param_promedio = models.BooleanField(help_text='Parametro de clasificacion 2')
	param_sm = models.BooleanField(help_text='Parametro de clasificacion 3')	
	numero_entradas = models.IntegerField(help_text='Num de turnos')
	lugar = models.CharField(max_length=100)
	direccion = models.CharField(max_length=100)
	zip_code = models.CharField(max_length=8)	
	telefono = models.CharField(max_length=15)
	celular = models.CharField(max_length=15,null=True,blank=True)
	fecha_inicio = models.DateField(help_text='Programe la fecha unica del torneo')	
	fecha_creacion = models.DateField(help_text='F creacion', verbose_name='Fecha Creacion',auto_now=True)

	def __unicode__(self):
		return self.nombre	
#	def __str__(self):
#		return '%s id=%s'% (self.nombre,self.id_torneo)

# tabla handicap
class Handicap(models.Model):
	id_handicap = models.AutoField(primary_key=True)
	id_torneo = models.ForeignKey(Torneo)
	id_categoria_juego = models.ForeignKey(CategoriaJuego)
	valor = models.IntegerField()


#---------------------------------------------------------------------------------
#tabla fases_partida : with DATA
class FasePartida(models.Model):
	id_fase_partida=models.AutoField(primary_key=True)
	descripcion = models.CharField(max_length=30)


# tabla grupos
class Grupo(models.Model):
	id_grupo = models.AutoField(primary_key=True)
	id_torneo = models.ForeignKey(Torneo)
	id_fase_partida = models.ForeignKey(FasePartida)
	descripcion = models.CharField(max_length=30,help_text="Ejem: grupo 01, grupo 02")
	distancia = models.IntegerField(help_text='de carambolas objetivo para ganar')
	num_set = models.IntegerField()
	
