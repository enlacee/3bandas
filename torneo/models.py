from django.db import models

class Pais(models.Model):
	id_pais = models.AutoField(primary_key=True) 
	descripcion = models.CharField(max_length=30)

class Torneo(models.Model):
	id_torneo = models.AutoField(primary_key=True) 
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()
	handicap = models.CharField(max_length=11)
	handicap_estado = models.BooleanField()
	numero_mesas = models.IntegerField()
	numero_entradas = models.IntegerField()
	numero_jugadores = models.IntegerField()
	param_puntos = models.IntegerField()
	param_promedio = models.IntegerField()
	param_sm = models.IntegerField()
	direccion = models.CharField(max_length=50)
	id_pais = models.ForeignKey(Pais)
	#id_estado = models.AutoField(Estado)
	estado = models.CharField(max_length=30)
	distrito = models.CharField(max_length=30)
	zip_code = models.CharField(max_length=8)
	telefono = models.CharField(max_length=15)




"""
Class Estado(models.Model):
	id_estado = models.AutoField(primary_key=true)
	descripcion = models.CharField(max_length=30)
"""