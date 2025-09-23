# ave.py
from mascota import Mascota

class Ave(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        super().__init__(id, apodo, fecha_ingreso) #use super pero puedo usar Mascota.__  - es super().__ o Mascota.__ sin ()
        self.dias_rehab = 0

    def saludar(self):
        return self.apodo + " canta: pio pio"
