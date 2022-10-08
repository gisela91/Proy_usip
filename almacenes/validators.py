#from django.db import models, ManyToManyField
#from .models import Proveedor
from django.core.exceptions import ValidationError
import datetime

def validar_par(value):
	if value % 2 !=0:
		raise ValidationError(
			'%(value)s no es un numero par',
			params={'value':value}
		)

def validar_nombre_categoria(value):
	if value == 'No permitido':
		raise ValidationError("No es una opcion permitida")


def validar_nombre_subject(value):
	if value == 'Comida':
		raise ValidationError("No es una opcion permitida")

#############################################################################
## ----Restringir restringir registro a un proveedor

def validar_nombre_proveedor(value):
	if value == "NUEVO":
		raise ValidationError("REGISTRO NO ACEPTADO")

###---Validar que la fecha de inicio de la oferta sea actual 
def validar_fechaInicio_oferta(value):
	dataHoy = datetime.date.today()
	if value < dataHoy:
		raise ValidationError("Esta fecha ya caduco")

#---Validar que la cantidad de pedido hacia un proveedor no sea mayor a 5
def validar_cantidad_pedido(value):
	if value > 5:
		raise ValidationError("EXCEDISTE EN LA CANTIDAD DE PEDIDO")




