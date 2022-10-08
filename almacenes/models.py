from django.db import models
from django.conf import settings
from .validators import validar_par
from .validators import validar_nombre_categoria
from .validators import validar_fechaInicio_oferta
from .validators import validar_cantidad_pedido
from .validators import validar_nombre_proveedor
from phonenumber_field.modelfields import PhoneNumberField

#from django.core.validators import EmailValidator

class Categoria(models.Model):
	nombre = models.CharField(max_length=100, unique=True, validators=[validar_nombre_categoria,])

	def __str__(self):
		return self.nombre

	class Meta:
		permissions = [
			("reporte_cantidad", "Visualizar el reporte de cantidad"),
			("reporte_detalle", "Reporte detallado de cantidades"),
		]


class ProductUnits(models.TextChoices):
	UNITS = 'u', 'Unidades'
	KG = 'kg', 'Unidades'

class Producto(models.Model):
	#validacion de email
	#nombre = models.CharField(max_length=100, unique=True,validators=[EmailValidator("Este no es un email valido")])
	nombre = models.CharField(max_length=100, unique=True)
	categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
	description = models.TextField()
	precio = models.DecimalField(decimal_places=2, max_digits=10, validators=[validar_par,])
	unidades = models.CharField(
		max_length=2,
		choices=ProductUnits.choices,
		default=ProductUnits.UNITS
	)
	disponible = models.BooleanField(blank=True, default=True)
	create = models.DateTimeField(auto_now_add=True)
	update = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Producto - %s" % self.nombre


class EstadoOrden(models.TextChoices):
	NOPAGADO = 'nopagado', 'No pagado'
	PAGADO = 'pagado', 'Pagado'

class Orden(models.Model):
	total = models.IntegerField(default=0)
	fecha = models.DateField()
	vendedor =  models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name="almacenes_orden_vendedor"
	)
	estado = models.CharField(
		max_length=10,
		choices=EstadoOrden.choices,
		default=EstadoOrden.NOPAGADO
	)

class OrdenProducto(models.Model):
	orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0)
	precio = models.DecimalField(decimal_places=2,max_digits=10)
	
############################################################################################

class Proveedor(models.Model):
	nomProveedor = models.CharField(
		max_length=100,
		unique=True,
		validators=[validar_nombre_proveedor])
	direccion = models.CharField(max_length=100, unique=True)
	telefono = PhoneNumberField(unique = True, null = False, blank = False) # Here
	
	def __str__(self):
		return "Proveedor - %s" % self.nomProveedor

#-------Validar que no se repita el proveedor al registrar

	def validar(self):
		proveedors = Proveedor.objects.filter(self.nomProveedor)	
		if proveedors :
			raise ValidationError("PROVEEDOR EXISTE")

class PedidoProveedor(models.Model):
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	cantidad = models.IntegerField(default=0, validators=[validar_cantidad_pedido,])
	fecha = models.DateField()

	def __str__(self):
		return "P - %s" % self.proveedor.nomProveedor

class Compras(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	pedproveedor = models.ForeignKey(PedidoProveedor, on_delete=models.CASCADE)

class EstadoOferta(models.TextChoices):
	DOSXUNO= 'dosxuno', '2 x 1'
	UNOREGALO = 'unoregalo', 'Un set de regalo'
	DIEZPORCIENTO = 'diezporciento', '10 % de rebaja'

class Ofertas(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	tipo = models.CharField(
		max_length=30,
		choices=EstadoOferta.choices,
		default=EstadoOferta.DOSXUNO
	)
	fechaInicio = models.DateField(validators=[validar_fechaInicio_oferta,])
	fechaFin = models.DateField()
