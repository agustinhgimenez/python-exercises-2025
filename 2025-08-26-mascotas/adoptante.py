# adoptante.py
class Adoptante:
    def __init__(self, nombre):
        self.nombre = nombre
        # contador por tipo
        self.mascotas_actuales = {"perro": 0, "gato": 0, "ave": 0}

    # en subclases se define la regla
    def puede_adoptar(self, tipo):
        return True

    def registrar_mascota(self, tipo):
        self.mascotas_actuales[tipo] += 1

    def total_mascotas(self):
        return (self.mascotas_actuales["perro"] +
                self.mascotas_actuales["gato"] +
                self.mascotas_actuales["ave"])
