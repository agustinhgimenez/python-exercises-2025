# peaje/__init__.py
from .peaje import Peaje
from .vehiculos import Vehiculo, Auto, Moto, AutoElectrico, Camion, Gubernamental
from .pagos import FormaDePago

__all__ = [
    "Peaje",
    "Vehiculo", "Auto", "Moto", "AutoElectrico", "Camion", "Gubernamental",
    "FormaDePago",
]
