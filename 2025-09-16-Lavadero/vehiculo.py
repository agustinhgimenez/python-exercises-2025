class Vehiculo:
    def __init__(self,suciedad):
        self.suciedad=suciedad

    def agregarSuciedad(self,cantSuciedad):
        self.suciedad += cantSuciedad
    
    def limpiar(self):
        self.suciedad=0

