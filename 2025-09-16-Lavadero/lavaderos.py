class LavaderoArtesanal:
    def __init__(self,cantidadEmpleados):
        self.tiempo = 0
        self.costoUnitario= 10 #Atributo de Clase
        self.cantidadEmpleados = cantidadEmpleados

    def calcularPrecio(self,vehiculo):
        return self.costoUnitario * self.cantidadEmpleados * round (vehiculo.suciedad / 5)
    
    def lavar(self,vehiculo):
        self.tiempo = round(vehiculo.suciedad / 5)
        print(self.calcularPrecio(vehiculo))
        vehiculo.limpiar()



class LavaderoAutomatico:
    def __init__(self):
        self.precio=1000 #precio fijo
        
    def lavar(self,vehiculo):
        vehiculo.limpiar()

    def calcularPrecio(self,vehiculo):
        return self.precio
    