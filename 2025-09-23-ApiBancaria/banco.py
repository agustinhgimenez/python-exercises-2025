
class Banco:
    def __init__(self):
        self.cuentas = []
        self.tarjetas = []

    def agregar_cuenta(self,cuenta):
        self.cuentas.append(cuenta)

    def agregar_tarjeta(self,tarjeta):
        self.tarjetas.append(tarjeta)

    def _buscar_cuenta(self, dni): #podria no usar listas y usar diccionario para evitar esto
        for c in self.cuentas:
            if c.dni == dni:
                return c
        raise OperacionInvalida("Cuenta inexistente")


    def _buscar_tarjeta(self, codigo_tarjeta): #podria no usar listas y usar diccionario para evitar esto
        for t in self.tarjetas:
            if t.codigo == codigo_tarjeta:
                return t
        raise OperacionInvalida("Tarjeta inexistente")


    def consumir(self,codigo_tarjeta,monto):
        tarjeta= self._buscar_tarjeta(codigo_tarjeta)
        tarjeta.consumir(monto)


    def consultar_saldo(self,dni):
        cuenta = self._buscar_cuenta(dni)
        return cuenta.monto_disponible

    def consultar_deuda(self,dni):
        cuenta=self._buscar_cuenta(dni)
        return cuenta.deuda

    def mejor_cliente(self):
        if not self.cuentas:
            raise OperacionInvalida("No hay cuentas registradas")
        return max(self.cuentas,key=lambda c:c.deuda).dni
