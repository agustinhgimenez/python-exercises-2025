# novato.py
from adoptante import Adoptante

class Novato(Adoptante):
    def __init__(self, nombre):
        super().__init__(nombre)  #use super pero puedo usar Adoptante.__ si uso mascota es con self
        self.limite_total = 1

    def puede_adoptar(self, tipo):
        return self.total_mascotas() < self.limite_total
