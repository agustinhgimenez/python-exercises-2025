# perro.py
from mascota import Mascota

class Perro(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        super().__init__(id, apodo, fecha_ingreso) #use super pero puedo usar Mascota.__ (debo pasar self en ese caso)
        self.dias_rehab = 30

    def saludar(self):
        return self.apodo + " ladra: guau!"
