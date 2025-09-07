#CLASE ABSTRACTA PADRE VEHICULO

class Vehiculo:
    def __init__(self,patente,formaDePago):
        self.patente=patente
        self.formaDePago=formaDePago
    
    def __str__(self):
        return self.patente


    def calcularTarifa(self): pass


# TIPOS VEHICULOS

class Auto(Vehiculo):
    valorAuto=100

    def calcularTarifa(self):
        return self.valorAuto


class Moto(Auto):

    def calcularTarifa(self):
        return self.valorAuto/2


class AutoElectrico(Auto):

    def calcularTarifa(self):
        return self.valorAuto*0.2

class Camion(Vehiculo):
    def __init__(self,patente,formaDePago,ejes):
        super().__init__(patente,formaDePago)
        self.ejes=ejes

    def calcularTarifa(self):
        return 200*self.ejes

class Gubernamental(Vehiculo):

    def calcularTarifa(self):
        return 0