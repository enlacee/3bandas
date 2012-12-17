#encoding:utf8
from django.forms import ModelForm
from django import forms

#Formulario apartir del modelo
from persona.models import Persona
from torneo.models import Estados,Pais

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona

		
""""		
class FormPersona (forms.Form):
	#error_css_class = 'error'
	#required_css_class = 'required'	
	nombre = forms.CharField(label='Nombre',initial='Nombre Completo')
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)
	tag = forms.CharField(max_length=2,required=True)

	def clean_message(self):
		mensaje = self.cleaned_data.get('mensaje','')
		num_words = len(mensaje.split())
		if num_words<4:
			raise forms.ValidationError("Solo # menor a 4")
		return mensaje
"""
		
		
		