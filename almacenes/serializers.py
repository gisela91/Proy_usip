from rest_framework import serializers
from .models import Categoria
from .models import Producto
from .models import Proveedor
from .models import PedidoProveedor
from .models import Ofertas
from .models import Compras
from .validators import validar_nombre_subject

class CategoriaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Categoria
		fields = "__all__"	

class ProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Producto
		fields = "__all__"	

class ReporteProductoSerializer(serializers.Serializer):
	cantidad = serializers.IntegerField()
	productos = ProductoSerializer(many=True)

class ContactSerializer(serializers.Serializer):
	email = serializers.EmailField()
	subject = serializers.CharField(max_length=100, validators=[validar_nombre_subject])
	body = serializers.CharField(max_length=255)

	###################################
class ProveedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = Proveedor
		fields = "__all__"

class PedidoProveedorSerializer(serializers.ModelSerializer):
	class Meta:
		model = PedidoProveedor
		fields = "__all__"

class OfertasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Ofertas
		fields = "__all__"	

class ComprasSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compras
		fields = "__all__"	

class ReporteComprasSerializer(serializers.Serializer):
	cantidad = serializers.IntegerField()
	compras = ComprasSerializer(many = True)
