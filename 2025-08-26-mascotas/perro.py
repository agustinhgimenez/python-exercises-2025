# perro.py
from mascota import Mascota

class Perro(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        Mascota.__init__(self, id, apodo, fecha_ingreso)
        self.dias_rehab = 30

    def saludar(self):
        return self.apodo + " ladra: guau!"
