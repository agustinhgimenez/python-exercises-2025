
from vehiculo import Vehiculo #Importo clase Vehiculo de vehiculo.py
from formacion import EstrategiaFormacion #importo clase EstrategiaFormacion de formacion.py

class Bandada:
    def __init__(self, formacion: EstrategiaFormacion):
        self.bandada = []
        self.formacion = formacion  # inyección de estrategia

    def ensuciar(self, auto: Vehiculo):
        self.formacion.ensuciar(auto, self.bandada)

    def cambiarFormacion(self, nuevaFormacion: EstrategiaFormacion):
        self.formacion = nuevaFormacion



class OtraAve:
    def ensuciar(self, vehiculo):
        vehiculo.suciedad += 50

class Paloma:
    def __init__(self, peso):
        self.peso = peso

    def ensuciar(self, vehiculo):
        vehiculo.suciedad += self.peso * 0.3
        self.peso = self.peso * 0.7

class Gaviota:
    def __init__(self, pescadoComido):
        self.pescadoComido = pescadoComido
    def ensuciar(self, vehiculo):
        vehiculo.suciedad += self.pescadoComido * 3