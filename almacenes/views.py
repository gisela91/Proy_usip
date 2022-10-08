from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import Categoria
from .models import Producto
from .models import Proveedor
from .models import PedidoProveedor
from .models import Ofertas
from .models import Compras
from .forms import ProductoForm
from .serializers import CategoriaSerializer
from .serializers import ProveedorSerializer
from .serializers import PedidoProveedorSerializer
from .serializers import ProductoSerializer
from .serializers import OfertasSerializer
from .serializers import ComprasSerializer
from .serializers import ReporteProductoSerializer
from .serializers import ReporteComprasSerializer
from .serializers import ContactSerializer
from .permissions import IsUserAlmacen
from .utils import permission_required
import logging

logger = logging.getLogger(__name__)
#logger = logging.getLogger("Nombre personalizado")

def index(request):
	return HttpResponse("Hola Mundo")

def contacto(request, nombre):
	return HttpResponse(f"Bienvenido {nombre} a la clase Django")

#def categoria(request):
#	categorias = Categoria.objects.all()
#	return render(request, "categorias.html", {"categorias": categorias})

def categoria(request):
	post_nombre = request.POST.get('nombre')
	if post_nombre:
		q = Categoria(nombre=post_nombre)
		q.save()
		#c=Categoria.objects.get(id=2)
		#q = Producto(nombre="Producto nuevo",precio="12",categoria=c)
		#q.save()
	filtro_nombre = request.GET.get("nombre")
	if filtro_nombre:
		categorias = Categoria.objects.filter(nombre__contains=filtro_nombre)
	else:
		categorias = Categoria.objects.all()
	#print(categorias.query)
	return render(request, "categorias.html", {"categorias": categorias})
#http://127.0.0.1:8000/almacenes/categorias/

def productoFormView(request):
	form = ProductoForm()
	producto = None

	id_producto = request.GET.get('id')
	if id_producto:
		#producto = Producto.objects.get(id=id_producto)
		producto = get_object_or_404(Producto, id=id_producto)
		form = ProductoForm(instance=producto)

	if request.method == 'POST':
		if producto:
			form = ProductoForm(request.POST, instance=producto)
		else:
			form = ProductoForm(request.POST)
	if form.is_valid():
		form.save()

	return render(request, "form_productos.html", {"form": form})

class CategoriaViewSet(viewsets.ModelViewSet):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer
	permission_classes = [IsUserAlmacen]

@permission_classes([IsAuthenticated])
class CategoriaCreateAndList(generics.CreateAPIView, generics.ListAPIView):
	queryset = Categoria.objects.all()
	serializer_class = CategoriaSerializer

@api_view(["GET"])
#@permission_classes([IsAuthenticated])
@permission_required(["almacenes.reporte_cantidad"])
def categoria_contador(request):
	'''
	cantidad de items en el modelo categoria
	'''
	logger.info("Cantidad categoria mostrada correctamente")
	try:
		cantidad = Categoria.objects.count()
		return JsonResponse(
			{
				"cantidad": cantidad
			},
			safe=False,
			status=200,
		)
	except Exception as e:
		return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def productos_tipo_unidad(request):
	'''
	Productos filtrados por tipo de unidad
	'''
	try:
		productos = Producto.objects.filter(unidades='u')
		return JsonResponse(
			ProductoSerializer(productos, many=True).data,
			safe=False,
			status=200,
			)
	except Exception as e:
		return JsonResponse({"mensaje": str(e)}, status=400)


@api_view(["GET"])
def reporte_productos(request):
	'''
	Reporte de Productos
	'''
	try:
		productos = Producto.objects.filter(unidades='u')
		cantidad = productos.count()

		return JsonResponse(
			ReporteProductoSerializer({
				"cantidad": cantidad,
				"productos": productos
			}).data,
			safe=False,
			status=200,
			)
	except Exception as e:
		return JsonResponse({"mensaje": str(e)}, status=400)


@api_view(["POST"])
def enviar_mensaje(request):
	'''
	Enviar mensajes via email
	'''
	cs =  ContactSerializer(data=request.data)
	if cs.is_valid():
		return JsonResponse({"mensaje": "Mensaje enviado satisfactoriamente"}, status=200)

	else:
		return JsonResponse({"mensaje": cs.errors}, status=200)

############################################################################

class ProveedorViewSet(viewsets.ModelViewSet):
	queryset = Proveedor.objects.all()
	serializer_class = ProveedorSerializer

class OfertasListAndDel(generics.ListAPIView, generics.DestroyAPIView):
	queryset = Ofertas.objects.all()
	serializer_class = OfertasSerializer

class PedidoList(generics.ListAPIView):
	queryset = PedidoProveedor.objects.all()
	serializer_class = PedidoProveedorSerializer

class ComprasListAndDel(generics.ListAPIView, generics.DestroyAPIView):
	queryset = Compras.objects.all()
	serializer_class = ComprasSerializer

@api_view(["GET"])
def ofertas_tipo_oferta(request):
	'''
	Ofertas filtradas por tipo de oferta
	'''
	try:
		oferta = Ofertas.objects.filter(tipo='diezporciento')
		return JsonResponse(
			OfertasSerializer(oferta, many=True).data,
			safe=False,
			status=200,
			)
	except Exception as e:
		return JsonResponse({"mensaje": str(e)}, status=400)

@api_view(["GET"])
def reporte_compras(request):
	'''
	Reporte y cantidad de compras del 'prodnuevo'
	'''
	try:
		producto=Producto.objects.get(nombre='prodnuevo')
		idprod = producto.id
		compras = Compras.objects.filter(producto=idprod)
		cantidad = compras.count()
		return JsonResponse(
			ReporteComprasSerializer({
				"cantidad": cantidad,
				"compras": compras
				}).data,
			safe=False,
			status=200,
			)
	except Exception as e:
		return JsonResponse({"mensaje": str(e)}, status=400)


