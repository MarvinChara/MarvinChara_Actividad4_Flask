from .extensions import appbuilder
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Categoria, Producto
class CategoriaModelView(ModelView):
    datamodel = SQLAInterface(Categoria)
    label_columns = { "nombre" : "Nombre",
                    "descripcion": "Descripcion",
                    "imagen": "Imagen",
                    "estado": "Estado",
                    "creado_en": "Creado en",
                    "actualizado_en":"Actualizado en"}
    list_columns= ["nombre", "descripcion", "estado", "creado_en"]
    
    add_columns = ["nombre", "descripcion", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "imagen", "estado", "creado_en","actualizado_en"]
    
class ProductoModelView(ModelView):
    datamodel = SQLAInterface(Producto)
    label_columns = { "nombre" : "Nombre",
                    "descripcion": "Descripcion",
                    "precio" : "Precio",
                    "categorias": "Categoria",
                    "imagen": "Imagen",
                    "estado": "Estado",
                    "creado_en": "Creado en",
                    "actualizado_en":"Actualizado en"}
    list_columns= ["nombre", "precio", "categorias", "estado"]
    add_columns = ["nombre", "descripcion","precio","categorias", "imagen", "estado"]
    edit_columns = ["nombre", "descripcion","precio","categorias", "imagen", "estado"]
    show_columns = ["nombre", "descripcion", "precio", "imagen", "estado", "creado_en","actualizado_en"]
    
appbuilder.add_view(
        CategoriaModelView,
        "Categorias",
        icon="fa-info",
        category="Configuraciones",
        category_icon="fa-info"
    )
    
appbuilder.add_view(
        ProductoModelView,
        "Productos",
        icon="fa-info",
        category="Configuraciones",
        category_icon="fa-info"
    )