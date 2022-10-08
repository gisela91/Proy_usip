from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"proveedores", views.ProveedorViewSet)


urlpatterns = [
	#path('contacto/<str:nombre>', views.contacto, name='contacto'),
	#path('', views.index, name='index'),
	#path('categorias/', views.categoria, name='categorias'),
	#path('productos/', views.productoFormView, name='productos'),
	path('mensaje/enviar', views.enviar_mensaje),
	
	path('productos/reporte', views.reporte_productos),
	path('productos/tipo/unidades', views.productos_tipo_unidad),
	path('categorias/cantidad', views.categoria_contador),
	path('categorias/create_list', views.CategoriaCreateAndList.as_view(), name='productos'),
	#####
	path('ofertas/list_delete', views.OfertasListAndDel.as_view(), name='ofertas'),
	path('compras/list_delete', views.ComprasListAndDel.as_view(), name='compras'),
	path('pedproveedor/list', views.PedidoList.as_view(), name='pedido'),
	path('ofertas/tipo', views.ofertas_tipo_oferta),
	path('compras/reporte', views.reporte_compras),
	
	path('', include(router.urls))
]