# gato.py
from mascota import Mascota

class Gato(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        super().__init__(id, apodo, fecha_ingreso) #use super pero puedo usar Mascota.__ si uso mascota es con self
        self.dias_rehab = 180

    def saludar(self):
        return self.apodo + " maulla: miau"
