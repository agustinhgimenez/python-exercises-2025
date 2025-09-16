
from abc import ABC, abstractmethod

class EstrategiaFormacion(ABC):
    @abstractmethod
    def ensuciar(self, vehiculo, aves):
        pass

# ======= Estrategias concretas =======

class FormacionV(EstrategiaFormacion):
    def ensuciar(self, vehiculo, aves):
        for ave in aves:
            ave.ensuciar(vehiculo)


class FormacionW(EstrategiaFormacion):
    def ensuciar(self, vehiculo, aves):
        for _ in range(2):  # dos pasadas
            for ave in aves:
                ave.ensuciar(vehiculo)


class FormacionI(EstrategiaFormacion):
    def ensuciar(self, vehiculo, aves):
        # primera y última
        aves[0].ensuciar(vehiculo)
        aves[-1].ensuciar(vehiculo)
