
class Persona:
    def __init__(self,temperatura,cantidad_celulas):
        self.temperatura = temperatura
        self.cantidad_celulas = cantidad_celulas
        self.enfermedades = [] # Lista
    
    def contraer(self,enfermedad):   #Cualquier persona puede contraer enfermedades  - Punto 1
        self.enfermedades.append(enfermedad)

    def vivir_un_dia(self): # en el momento que contrae no causa efecto, pero cada dia que vive una persona con su enfermedad se producen sus consecuencias - Punto 1
        for enfermedad in list(self.enfermedades):
            enfermedad.afectar(self)

    def recibir_medicamento(self,medicamento): # cuando la persona reciba un medicamento, las enfermedades se atenuan en la cantidad de medicamento recibida multiplicada por 15 - Punto 3
        dosis = int(medicamento) * 15
        for enfermedad in self.enfermedades:
            enfermedad.atenuar(dosis)

    def esta_sana(self): # la persona esta sana si todas sus enfermedades estan curadas - Punto 2 
    
        return all(enfermedad.esta_curada() for enfermedad in self.enfermedades)

    def eliminar_curadas(self): #quitar del listado las enfermedades ya curadas - Opcional

        self.enfermedades = [enfermedad for enfermedad in self.enfermedades if not enfermedad.esta_curada()]
    
 