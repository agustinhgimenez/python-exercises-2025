# refugio.py
class Refugio:
    def __init__(self):
        self.adoptantes = set()
        self.mascotas = set()

    def mascotas_disponibles(self):
        # por ahora, todas las cargadas
        return list(self.mascotas)

    def agregar_mascota(self, mascota):
        self.mascotas.add(mascota)

    def adoptar_mascota(self, mascota):
        #self.mascotas.add(refugio)
        self.mascotas.remove(mascota)

    def agregar_adoptante(self, adoptante):
        self.adoptantes.add(adoptante)

    def eliminar_adoptante(self, adoptante):
        self.adoptantes.remove(adoptante)

    def __len__(self):
        return len(self.mascotas)

    def __str__(self):
        if not self.mascotas:
            return "Refugio vacío"
        return "Refugio con mascotas:\n" + "\n".join(f"- {m}" for m in self.mascotas)
