from django.contrib import admin
from .models import Categoria
from .models import Producto
from .models import Orden
from .models import OrdenProducto
from .models import Proveedor
from .models import PedidoProveedor
from .models import Compras
from .models import Ofertas

class ProductoAdmin(admin.ModelAdmin):
	list_display = ("nombre", "categoria", "precio", "unidades")
	ordering = ["precio"]
	search_fields = ["nombre"]
	list_filter = ("disponible", "precio")
	
class ProveedorAdmin(admin.ModelAdmin):
	list_display = ("nomProveedor", "direccion", "telefono")

class PedidoProveedorAdmin(admin.ModelAdmin):
	list_display = ("proveedor", "cantidad", "fecha")

class ComprasAdmin(admin.ModelAdmin):
	list_display = ("producto", "pedproveedor")

class OfertasAdmin(admin.ModelAdmin):
	list_display = ("producto", "tipo", "fechaInicio", "fechaFin")

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden)
admin.site.register(OrdenProducto)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(PedidoProveedor, PedidoProveedorAdmin)
admin.site.register(Compras, ComprasAdmin)
admin.site.register(Ofertas, OfertasAdmin)
# Register your models here.
