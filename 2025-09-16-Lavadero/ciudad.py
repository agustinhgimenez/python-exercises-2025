class Ciudad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.lavaderos=[]
        self.vehiculos=[]

    def encontrarLavaderoEconomico(self,vehiculo):
        minimo=None
        nombre= None
        for lavadero in self.lavaderos:
            if(minimo is None or lavadero.calcularPrecio(vehiculo) < minimo):
                minimo = lavadero.calcularPrecio(vehiculo)
                nombre = lavadero
        return nombre

    def ensuciarConCeniza(self,cantidadMilimetros):
        for auto in self.vehiculos:
            auto.suciedad += cantidadMilimetros

    