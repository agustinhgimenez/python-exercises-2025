# gato.py
from mascota import Mascota

class Gato(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        Mascota.__init__(self, id, apodo, fecha_ingreso)
        self.dias_rehab = 180

    def saludar(self):
        return self.apodo + " maulla: miau"
