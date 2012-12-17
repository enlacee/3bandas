from django.db import models
#from persona.models import Persona
"""
# tabla admin			
class Admin(models.Model):
	id_admin = models.AutoField(primary_key=True)
	id_persona = models.ForeignKey(Persona)
	email = models.EmailField()
	password = models.CharField(max_length=15)
	fecha_creacion = models.DateField(auto_now=True)
	
	def __str__(self):
		return self.id_admin"""