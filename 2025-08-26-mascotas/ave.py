# ave.py
from mascota import Mascota

class Ave(Mascota):
    def __init__(self, id, apodo, fecha_ingreso):
        Mascota.__init__(self, id, apodo, fecha_ingreso)
        self.dias_rehab = 0

    def saludar(self):
        return self.apodo + " canta: pio pio"
