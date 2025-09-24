from abc import ABC,abstractmethod

class OperacionInvalida(Exception):
    pass

class EstrategiaTarjeta(ABC):
    @abstractmethod
    def consumir(self,cuenta,monto):
        pass


class Tarjeta:
    def __init__(self,codigo,cuenta,estrategia: EstrategiaTarjeta):
        self.codigo=codigo
        self.cuenta=cuenta
        self.estrategia = estrategia

    
    def consumir(self,monto):
        #delega la logica a la estrategia
        self.estrategia.consumir(self.cuenta,monto)

class DebitoEstrategia(EstrategiaTarjeta):
    """
    - Descuenta del saldo disponible de la cuenta.
    - Si el monto > 3000, se aplica devolución de IVA 21%:
      se cobra 0.79 * monto.
    """
    def consumir(self,cuenta,monto):
        if monto <= 0:
            raise OperacionInvalida("Monto inválido")
        monto_cobrar = monto * 0.79 if monto > 3000 else monto
        cuenta.descontar(monto_cobrar)


class CreditoBlanca(EstrategiaTarjeta):
    """
    - Límite de deuda total = 10000 (sobre la CUENTA, no solo esta tarjeta).
    - Incrementa la deuda si no supera el tope.
    """
    LIMITE = 10_000
    def consumir(self,cuenta,monto):
        if monto <= 0:
            raise OperacionInvalida("Monto inválido")
        if cuenta.deuda + monto > self.LIMITE:
            raise OperacionInvalida("Se supera el tope de deuda de la tarjeta Blanca")
        cuenta.aumentar_deuda(monto)
    

class CreditoDorada(EstrategiaTarjeta):
    """
    - Sin tope de deuda.
    - Incrementa la deuda.
    """
    def consumir(self,cuenta,monto):
         if monto <= 0:
            raise OperacionInvalida("Monto inválido")
         cuenta.aumentar_deuda(monto)