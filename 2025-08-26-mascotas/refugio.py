# refugio.py
class Refugio:
    def __init__(self):
        self.mascotas = []     # en refugio
        self.adopciones = []   # historial

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

    def listar_disponibles(self):
        res = []
        for m in self.mascotas:
            if m.disponible():
                res.append(m)
        return res

    def _tipo(self, mascota):
        nombre = mascota.__class__.__name__.lower() #use super pero puedo usar mascota.__
        if nombre in ("perro", "gato", "ave"):
            return nombre
        return "desconocido"

    def registrar_adopcion(self, adopcion):
        mascota = adopcion.mascota
        adoptante = adopcion.adoptante

        if mascota not in self.mascotas:
            raise ValueError("La mascota no está en el refugio.")
        if not mascota.disponible():
            raise ValueError("La mascota aún no está disponible.")

        tipo = self._tipo(mascota)
        if not adoptante.puede_adoptar(tipo):
            raise ValueError("El adoptante no cumple los límites.")

        adoptante.registrar_mascota(tipo)
        self.mascotas.remove(mascota)
        self.adopciones.append(adopcion)

    def historial_adopciones(self):
        return self.adopciones
