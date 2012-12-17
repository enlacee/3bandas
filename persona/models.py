from django.db import models
from torneo.models import Estados,Pais

# tabla tipos_documentos
class TipoDocumento(models.Model):
	cod_tipo_documento = models.CharField(max_length=2,primary_key=True)
	descripcion = models.CharField(max_length=40)
	descripcion_abreviada = models.CharField(max_length=10)

# tabla ubigeo_departamentos
class UbigeoDepartamento(models.Model):
	cod_departamento =  models.CharField(max_length=2,primary_key=True)
	descripcion = models.CharField(max_length=30)

# tabla ubigeo_provincias
class UbigeoProvincia(models.Model):
	cod_provincia = models.CharField(max_length=4,primary_key=True)
	descripcion = models.CharField(max_length=30)

# tabla cod_ubigeo_reniec
class UbigeoReniec(models.Model):
	cod_ubigeo_reniec = models.CharField(max_length=6,primary_key=True)
	cod_departamento = models.ForeignKey(UbigeoDepartamento)
	cod_provincia = models.ForeignKey(UbigeoProvincia)
	descripcion = models.CharField(max_length=30)

# tabla personas
class Persona(models.Model):
	GENERO_CHOICES =(
		('M','Maculino'),
		('F','Femenino')
		)
	id_persona = models.AutoField(primary_key=True)
	id_pais = models.ForeignKey(Pais)
	id_estado = models.ForeignKey(Estados)
	cod_tipo_documento = models.ForeignKey(TipoDocumento)
	nombre = models.CharField(max_length=30)
	apellido_parterno = models.CharField(max_length=30)
	apellido_materno = models.CharField(max_length=30)
	fecha_nacimiento = models.DateField()
	num_documento = models.CharField(max_length=30)
	sexo = models.CharField(max_length=1,choices=GENERO_CHOICES)
	direccion_residencia = models.CharField(max_length=100)
	direccion_estadia = models.CharField(max_length=100)
	telefono = models.CharField(max_length=15,null=True,blank=True)
	celular = models.CharField(max_length=15,null=True,blank=True)
	correo = models.EmailField()
	imagen = models.FileField(upload_to='personas', verbose_name='Imagen')
	fecha_creacion = models.DateField(auto_now=True)
	def __str__(self):
		return self.nombre