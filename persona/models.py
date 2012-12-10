from django.db import models

class Persona(models.Model):
	GENERO_CHOICES =(
		('M','Maculino'),
		('F','Femenino')
		)
	id_persona = models.AutoField(primary_key=True) 
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
	def __unicode__(self):
		return self.nombre