from abc import ABC , abstractmethod

class EstrategiaRecargo(ABC):
    @abstractmethod
    def agregar_recargo(self,envio):
        pass


class RecargoCategorico(EstrategiaRecargo): #Si el envío tiene una categoría X, se computa un porcentaje dado del precio base, por ejemplo 10% para la tecnología (por frágil).

    def agregar_recargo():


class RecargoSobrePeso(EstrategiaRecargo): # Si el peso es mayor a un peso dado (1kg) se le suma $80.

    def agregar_recargo():


class RecargoArbitrario(EstrategiaRecargo): # $50 adicionales, ejemplo: por el Día del Trabajador de Correo.

    def agregar_recargo():


# podria haber mas recargos