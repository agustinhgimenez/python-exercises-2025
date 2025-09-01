# novato.py
from adoptante import Adoptante

class Novato(Adoptante):
    def __init__(self, nombre):
        Adoptante.__init__(self, nombre)
        self.limite_total = 1

    def puede_adoptar(self, tipo):
        return self.total_mascotas() < self.limite_total
