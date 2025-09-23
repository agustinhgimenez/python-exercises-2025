from abc import ABC , abstractmethod

class EstrategiaImpuesto(ABC):
    @abstractmethod
    def agregar_impuesto(self,envio)
        pass


class IVA(EstrategiaImpuesto):  # IVA: 20% del precio neto.
 
    def agregar_impuesto():


class ImpuestoMulticategoria(EstrategiaImpuesto): #  1% del precio neto, se aplica cuando el envío tiene más de 3 categorías.

    def agregar_impuesto():


class ImpuestoAduanero(EstrategiaImpuesto): # 50%, pero sólo cuando el envío es internacional. Un pedido es internacional cuando los países de origen y destino difieren.

    def agregar_impuesto():


class ImpuestoExtrano(EstrategiaImpuesto): # 10%, sólo si tiene precio base es par.

    def agregar_impuesto():



#podria haber otros