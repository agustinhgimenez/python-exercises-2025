class FormaDePago:
    def __init__(self,porcentaje):
        self.porcentaje=porcentaje
    
    def calcularCobro(self,vehiculo):
        return vehiculo.calcularTarifa() * self.porcentaje
