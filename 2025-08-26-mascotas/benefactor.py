# benefactor.py
from adoptante import Adoptante

class Benefactor(Adoptante):
    def __init__(self, nombre):
        super().__init__(nombre) #use super pero puedo usar Adoptante.__ si uso Adoptante es con self
        self.limite_perros = 2
        self.limite_gatos = 3
        self.limite_aves = 5

    def puede_adoptar(self, tipo):
        if tipo == "perro":
            return self.mascotas_actuales["perro"] < self.limite_perros
        if tipo == "gato":
            return self.mascotas_actuales["gato"] < self.limite_gatos
        if tipo == "ave":
            return self.mascotas_actuales["ave"] < self.limite_aves
        return False
