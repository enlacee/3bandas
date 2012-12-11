#encoding:utf8
#from django import newforms as forms?????????
from django.forms import ModelForm
#Formulario apartir del modelo
from torneo.models import Torneo, Pais
from django import forms




TOPIC_CHOICES = (
	('general','General enquiry'),
	('bug','Bug report'),
	('suggestion','Suggestion'),
)

class ContactForm (forms.Form):
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



#formulario Torneo
DATA_CHOICES = (
	('01','01'),
	('02','02'),
	('03','03'),
	('04','04'),
	('05','05'),
	('06','06'),
	('07','07'),
	('08','08'),
	('09','09'),
	('10','10'),
)
NUM_JUGADORES = (
	('24','24'),
	('30','30'),
	('32','32'),
	('36','36'),
	('40','40'),
	('45','45'),
	('48','48'),
	('60','60'),
	('72','72'),
	('96','96'),	

)
class TorneoFrm(forms.ModelForm):
    class Meta:
        model = Torneo

"""
class TorneoFrm(forms.Form):
	nombre = forms.CharField(label='NOMBRE DEL TORNEO')
	descripcion = forms.CharField(widget=forms.Textarea)
	handicap_A = forms.Select(choices=DATA_CHOICES)
	handicap_B = forms.Select(choices=DATA_CHOICES)
	handicap_C = forms.Select(choices=DATA_CHOICES)
	handicap_D = forms.Select(choices=DATA_CHOICES)
	handicap_estado = forms.BooleanField(label='HANDICAP ESTADO')
	numero_mesas = forms.CharField()
	numero_jugadores = forms.Select(choices=NUM_JUGADORES)
	param_puntos = forms.BooleanField(default=True)
	param_promedio = forms.BooleanField(help_text='Parametro de clasificacion 2')	
	param_sm = forms.BooleanField(help_text='Parametro de clasificacion 3')
	#distancia = models.IntegerField(help_text='de carambolas objetivo para ganar')
	numero_entradas = forms.IntegerField(help_text='Num de turnos')
	lugar = forms.CharField(max_length=100)
	direccion = forms.CharField(max_length=100)
	zip_code = forms.CharField(max_length=8)	
	telefono = forms.CharField(max_length=15)
	celular = forms.CharField(max_length=15,null=True,blank=True)
	fecha_inicio = forms.DateField(help_text='Programe la fecha unica del torneo')	
"""