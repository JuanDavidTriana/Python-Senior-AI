from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database.database import Base # permite la conexion a la base de datos

class TipoVehiculoORM(Base):
    __tablename__ = "tipo_vehiculos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), unique=True, nullable=False)
    tarifa = Column(Float, nullable=False)
    limite = Column(Integer, nullable=False)
    estado = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    vehiculos = relationship("VehiculoORM", back_populates="tipo_vehiculos")

class VehiculoORM(Base):
    __tablename__ = "vehiculo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_tipovehiculo = Column(Integer, ForeignKey("tipo_vehiculos.id"), nullable=False)
    placa = Column(String(10),nullable=False)
    documento = Column(String(100), nullable=False)
    nombre = Column(String(100), nullable=False)
    hora_llegada = Column(TIMESTAMP, nullable=False, server_default=func.now())
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    tipo_vehiculo = relationship("TipoVehiculoORM", back_populates="vehiculo")
    pagos = relationship("PagoORM", back_populates="vehiculo")
    
class PagoORM(Base):
    __tablename__ = "pagos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    id_vehiculo = Column(Integer, ForeignKey("vehiculo.id"), nullable=False)
    pago = Column(Float,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    vehiculo = relationship("VehiculoORM", back_populates="pagos")