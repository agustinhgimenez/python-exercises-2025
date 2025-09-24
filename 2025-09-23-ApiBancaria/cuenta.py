class Cuenta:
    def __init__(self,dni,monto_disponible,deuda):
        self.dni=dni
        self.monto_disponible=monto_disponible
        self.deuda=deuda

    def descontar(self,monto):
        if monto<0:
            raise OperacionInvalida("Monto Negativo")
        if self.monto_disponible < monto:
            raise OperacionInvalida("Saldo Insuficiente")
        self.monto_disponible -=monto

    def aumentar_deuda(self,monto):
        if monto<0:
            raise OperacionInvalida("Monto Negativo")
        self.deuda +=monto


