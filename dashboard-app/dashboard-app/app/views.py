from .extensions import appbuilder, db
from flask_appbuilder import BaseView, ModelView, expose
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Categoria, Producto, Venta

class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    label_columns = { 
        "nombre" : "Nombre",
        "descripcion": "Descripcion",
        "imagen": "Imagen/Logo",
        "estado": "Estado",
        "creado_en": "Fecha de Creación",
        "actualizado_en":"Última Actualización"
    }
    
    # CAMBIO: Agregamos "imagen" y "actualizado_en" a la lista para que el docente vea el resultado
    list_columns = ["nombre", "imagen", "estado", "creado_en", "actualizado_en"]
    
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen", "estado", "creado_en","actualizado_en"]
    
class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    label_columns = { 
        "nombre" : "Nombre",
        "descripcion": "Descripcion",
        "precio" : "Precio",
        "categorias": "Categoría",
        "imagen": "Foto del Producto",
        "estado": "Estado",
        "creado_en": "Fecha de Creación",
        "actualizado_en":"Última Actualización"
    }
    
    # CAMBIO: Agregamos "imagen" y "actualizado_en" para que sean visibles en la tabla principal
    list_columns = ["nombre", "precio", "categorias", "imagen", "estado", "actualizado_en"]
    
    add_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "precio", "categorias", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "imagen", "estado", "creado_en","actualizado_en"]
    
class VentaModelView(ModelView):
    datamodel = SQLAInterface(Venta)    
    # CAMBIO: Mostramos la fecha completa para verificar que se guarde bien
    list_columns = ["producto", "cantidad", "precio_unitario", "total", "fecha"]
    add_columns = ["producto", "cantidad", "precio_unitario", "total"]
    edit_columns = ["producto", "cantidad", "precio_unitario", "total"]
    
# REPORTES
class ReporteView(BaseView):
    route_base = '/reportes'    
    @expose("/")
    def index(self):
        total_ventas = db.session.query(Venta).count()
        total_ingresos = db.session.query(
                db.func.sum(Venta.total)
            ).scalar() or 0
        venta_por_producto = db.session.query(
                Venta.producto,
                db.func.sum(Venta.cantidad)
            ).group_by(Venta.producto).all()
        return self.render_template("reportes.html",
                                    t_ventas = total_ventas,
                                    t_ingresos = total_ingresos,
                                    venta_por_producto = venta_por_producto
                                    )
        
appbuilder.add_view(
        CategoriaModelView,
        "Categorias",
        icon="fa-folder-open",
        category="Configuraciones"
    )
    
appbuilder.add_view(
        ProductoModelView,
        "Productos",
        icon="fa-barcode",
        category="Configuraciones"
    )

appbuilder.add_view(
        VentaModelView,
        "Ventas",
        icon="fa-shopping-cart",
        category="Operaciones"
    )

appbuilder.add_view_no_menu(ReporteView())

appbuilder.add_link(
    "Reporte General",
    href="/reportes/",
    icon="fa-chart-line",
    category="Reportes"
)