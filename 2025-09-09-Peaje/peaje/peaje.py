from .vehiculos import Vehiculo

class Peaje:
    def __init__(self,nombre):
        self.nombre=nombre
        self.actividad=[]
        self.clientes=[]


    def cobrar(self,vehiculo):
        self.actividad.append(vehiculo)
        if vehiculo not in self.clientes:
            self.clientes.append(vehiculo)
        return vehiculo.formaDePago.calcularCobro(vehiculo)

    def recaudacionTotal(self):
        total=0
        for vehiculo in self.actividad:
            total+= vehiculo.formaDePago.calcularCobro(vehiculo)
        return total


    def totalVehiculo(self,vehiculoActual):
        subtotal=0
        for vehiculo in self.actividad:
            if vehiculo==vehiculoActual:
                subtotal+=vehiculo.formaDePago.calcularCobro(vehiculo)
        return subtotal
    
    def mejorCliente(self):
        return max(self.clientes, key=lambda vehiculo: self.totalVehiculo(vehiculo))