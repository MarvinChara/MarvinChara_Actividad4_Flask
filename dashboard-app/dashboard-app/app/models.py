import datetime
from flask_appbuilder import Model
from sqlalchemy import Boolean, Column, DateTime, Integer, Numeric, String, ForeignKey, Text
from sqlalchemy.orm import relationship

class Categoria(Model):
    __tablename__="categoria"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    imagen = Column(String(255), nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=datetime.UTC ,nullable=False)
    actualizado_en = Column(DateTime, default=datetime.UTC, onupdate= datetime.UTC, nullable=False)
    
    productos = relationship(
        "Producto",
        back_populates="categorias"
    )
    
    def __repr__(self):
        return  self.nombre
    
class Producto(Model):
    __tablename__="producto"
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10, 2), nullable=True)
    categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=False)
    imagen = Column(String(255), nullable=True)
    estado = Column(Boolean, nullable=True)
    creado_en = Column(DateTime, default=datetime.UTC ,nullable=False)
    actualizado_en = Column(DateTime, default=datetime.UTC, onupdate= datetime.UTC, nullable=False)
    categorias = relationship(
        "Categoria",
        back_populates="productos"
    )
    
    def __repr__(self):
        return  self.nombre

class Venta (Model):
    __tablename__="venta"
    id = Column(Integer, primary_key=True)
    producto = Column(String(150), nullable=False)
    cantidad = Column(Integer, nullable=False)
    precio_unitario = Column(Numeric(10, 2), nullable=True)
    total = Column(Numeric(10, 2), nullable=True)
    fecha = Column(DateTime, default=datetime.datetime.utcnow, onupdate= datetime.UTC, nullable=False)