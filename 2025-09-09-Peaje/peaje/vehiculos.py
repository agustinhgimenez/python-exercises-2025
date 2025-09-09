#CLASE ABSTRACTA PADRE VEHICULO
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self,patente,formaDePago):
        self.patente=patente
        self.formaDePago=formaDePago
    
    def __str__(self):
        return self.patente

    @abstractmethod #ACLARAR QUE ES ABSTRACTO , SI NO ESTA MAL
    def calcularTarifa(self): pass


# TIPOS VEHICULOS

class Auto(Vehiculo):
    valorAuto=100 #variable de clase (Statica compartida por todas las instancias) , si es self. es variable de instancia

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

    def calcularTarifa(self): #todos tienen que usar self , si o si iguales (si uno usa self,ejes todos tienen que usar self,ejes) . Si alguno impone algo mas como ejes , por ejemplo se utiliza en todas las clases aunque los otros no las utilicen
        return 200*self.ejes

class Gubernamental(Vehiculo):

    def calcularTarifa(self):
        return 0