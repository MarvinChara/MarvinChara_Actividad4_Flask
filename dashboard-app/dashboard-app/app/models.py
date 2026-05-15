import datetime
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn # IMPORTANTE: Para subir imágenes
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Categoria(Model):
    __tablename__="categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    # CAMBIO: Usamos ImageColumn para que aparezca el botón de "Examinar"
    imagen = Column(ImageColumn, nullable=True) 
    estado = Column(Boolean, nullable=True)
    # CAMBIO: Usamos datetime.datetime.now para capturar la hora real local
    creado_en = Column(DateTime, default=datetime.datetime.now, nullable=False)
    actualizado_en = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    
    productos = relationship(
        "Producto",
        back_populates="categorias"
    )
    
    def __repr__(self):
        return self.nombre
    
class Producto(Model):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    # CAMBIO: Usamos ImageColumn para habilitar la subida de archivos
    imagen = Column(ImageColumn, nullable=True) 
    estado = Column(Boolean, nullable=True)
    # CAMBIO: Corregidas las funciones de fecha
    creado_en = Column(DateTime, default=datetime.datetime.now, nullable=False)
    actualizado_en = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, nullable=False)
    
    categorias = relationship(
        "Categoria",
        back_populates="productos"
    )
    
    def __repr__(self):
        return self.nombre

class Venta (Model):
    __tablename__="venta"
    id = Column(Integer, primary_key=True)
    producto = Column(String(150), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=True)
    total = Column(Numeric(10, 2), nullable=True)
    # CAMBIO: Consistencia en el campo fecha
    fecha = Column(DateTime, default=datetime.datetime.now, nullable=False)