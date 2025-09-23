# mascota.py
from datetime import date

class Mascota:
    def __init__(self, id, apodo, fecha_ingreso):
        self.id = id
        self.apodo = apodo
        self.fecha_ingreso = fecha_ingreso
        self.dias_rehab = 0  # cada subclase lo cambia

    def saludar(self):
        return self.apodo + " saluda."

    def dias_en_refugio(self):
        hoy = date.today()
        return (hoy - self.fecha_ingreso).days

    def esta_rehabilitada(self):
        return self.dias_en_refugio() >= self.dias_rehab

    def disponible(self):
        return self.esta_rehabilitada()
