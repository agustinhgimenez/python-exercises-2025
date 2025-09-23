from persona import Persona
from abc import ABC,abstractmethod

class EstrategiaEnfermedad(ABC):
    @abstractmethod
    def afectar_persona(self, enfermedad, persona):
        """
        Aplica el efecto de la enfermedad 'enfermedad' sobre la persona 'persona'.
        """
        pass


class Enfermedad:
    def __init__(self,nombre,celulas_amenazadas,estrategia: EstrategiaEnfermedad):
        self.nombre = nombre
        self.celulas_amenazadas = celulas_amenazadas
        self.estrategia = estrategia


    def afectar(self,persona): # Punto 1 , hacer efecto
    #delego el comportamiento a la strategy
        self.estrategia.afectar_persona(self,persona)

    def atenuar(self,cantidad): # Cuando una enfermedad se atenua  , baja la cantidad de celulas amenazadas por ella" - Punto 2 Resta las celulas amenazadas
        self.celulas_amenazadas = max(0, self.celulas_amenazadas - int(cantidad)) #el max(0,..), permite que nunca sea <0

    def esta_curada(self): # Una enfermedad se considera curada si no amenaza a ninguna celula" - Devuelve true si ya no amenaza celulas # Punto 2 
        return self.celulas_amenazadas <= 0


class EnfermedadInfecciosa(EstrategiaEnfermedad):
    def afectar_persona(self, enfermedad, persona):
        # Regla 1: aumenta la temperatura en la milésima parte de las células amenazadas
        persona.temperatura += enfermedad.celulas_amenazadas / 1000.0
        # Regla 2: se reproduce a sí misma → duplica las células amenazadas
        enfermedad.celulas_amenazadas *= 2


class EnfermedadAutoinmune(EstrategiaEnfermedad):
    def afectar_persona(self, enfermedad, persona):
        # Regla: destruye la cantidad de células amenazadas (sin quedar negativo)
        persona.cantidad_celulas = max(0, persona.cantidad_celulas - enfermedad.celulas_amenazadas)


class EnfermedadMixta(EstrategiaEnfermedad): # Punto 4 teorico aplicado
    def afectar_persona(self, enfermedad, persona):
        # Aplico primero la parte infecciosa
        EnfermedadInfecciosa().afectar_persona(enfermedad, persona)
        # Luego la parte autoinmune
        EnfermedadAutoinmune().afectar_persona(enfermedad, persona)
