
class Vehiculo:
    def __init__(self, suciedad):
        self.suciedad = suciedad

    def agregarSuciedad(self, cantSuciedad):
        self.suciedad += cantSuciedad
    def limpiar(self):
        self.suciedad = 0

class LavaderoArtesanal:
    def __init__(self, cantidadEmpleados):
        self.tiempo = 0
        self.costoUnitario = 10 #Atributo de clase
        self.cantidadEmpleados = cantidadEmpleados

    def calcularPrecio(self, vehiculo):
        return self.costoUnitario * self.cantidadEmpleados * round(vehiculo.suciedad / 5)

    def lavar(self, vehiculo):
        self.tiempo = round(vehiculo.suciedad / 5)
        print(self.calcularPrecio(vehiculo))
        vehiculo.limpiar()

class LavaderoAutomatico:
    def __init__(self):
        self.precio = 1000 # precio fijo

    def lavar(self, vehiculo):
        vehiculo.limpiar()

    def calcularPrecio(self, vehiculo):
        return self.precio

class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lavaderos = []
        self.vehiculo = []

    def ensuciarConCeniza(self, cantidadMilimetros):
        for auto in self.vehiculo:
            auto.suciedad += cantidadMilimetros

    def encontrarLavaderoEconomico(self, vehiculo):
        minimo = None
        nombre = None
        for lavadero in self.lavaderos:
            if (minimo is None or lavadero.calcularPrecio(vehiculo) < minimo):
                minimo = lavadero.calcularPrecio(vehiculo)
                nombre = lavadero
        return nombre

class Bandada:
    def __init__(self, formacion):
        self.bandada = []
        self.formacion = formacion

    def ensuciar(self, auto):
        if self.formacion == "V":
            fv = FormacionV()
            fv.ensuciar(auto, self.bandada)
        elif self.formacion == "W":
            fw = FormacionW()
            fw.ensuciar(auto, self.bandada)
        else:
            fi = FormacionI()
            fi.ensuciar(auto, self.bandada)

    def cambiarFormacion(self, nuevaFormacion):
        self.formacion = nuevaFormacion

class FormacionV:
    def ensuciar(self, vehiculo, bandada):
        for ave in bandada:
            ave.ensuciar(vehiculo)
class FormacionW:
    def ensuciar(self, vehiculo, bandada):
        i = 1
        while i <= 2:
            for ave in bandada:
                ave.ensuciar(vehiculo)
            i += 1
class FormacionI:
    def ensuciar(self, vehiculo, bandada):
        bandada[0].ensuciar and bandada[-1].ensuciar

# No esta justificado heredar, porque NO se reutiliza nada

class OtraAve:
    def ensuciar(self, vehiculo):
        vehiculo.suciedad += 50

class Paloma:
    def __init__(self, peso):
        self.peso = peso

    def ensuciar(self, vehiculo):
        vehiculo.suciedad += self.peso * 0.3
        self.peso = self.peso * 0.7

class Gaviota:
    def __init__(self, pescadoComido):
        self.pescadoComido = pescadoComido
    def ensuciar(self, vehiculo):
        vehiculo.suciedad += self.pescadoComido * 3

# CONSIGNAS DE TRABAJO
# Crear una bandada de 2 Gaviotas, 1 Paloma, 1 Cotorra, 2 Loros en forma de V
gaviota1 = Gaviota(30)
gaviota2 = Gaviota(20)
paloma1 = Paloma(300)
cotorra1 = OtraAve()
loro1 = OtraAve()
loro2 = OtraAve()

bandadaInicial = Bandada("V")
bandadaInicial.bandada.extend([gaviota1, gaviota2, paloma1, cotorra1, loro1, loro2])

# Crear un auto limpio y ubicarlo en Bs As
auto1 = Vehiculo(0) #Inicialmente esta limpio
BuenosAires = Ciudad("Buenos Aires")
BuenosAires.vehiculo.append(auto1)

# Crear un lavadero de 3 trabajadores artesanal

SmallLav = LavaderoArtesanal(3) #Lavadero con 3 empleados
BuenosAires.lavaderos.append(SmallLav)

# TEST
# 4.a Que pase una paloma gorda por encima del auto

palomaG = Paloma(500)
palomaG.ensuciar(auto1)
print(auto1.suciedad)

# 4.b Que la bandada ensucie el auto: G1(90), G2(60), P1(90), 3 aves mas (150)... Total: 390
# 390 + la suciedad de antes (150) = 540!!

bandadaInicial.ensuciar(auto1)
print(auto1.suciedad)

# 4.c Que sobre Buenos Aires caiga una lluvia de ceniza volcánica

auto2 = Vehiculo(0)
BuenosAires.vehiculo.append(auto2) # Ahora tengo 2 autos en BsAs
BuenosAires.ensuciarConCeniza(100) # Cae una lluvia de ceniza de 100mm
print(auto1.suciedad, auto2.suciedad)

# 4.d Llevar el auto a SmallLav, hacerlo lavar y saber cuanto costo

SmallLav.lavar(auto1)   # Suciedad auto1 640, entonces tiempo(640/5 = 128) * 3 personas * 10 (costoUnitario) = 3840

# 4.e Que la bandada cambie su formacion de V a W y pase por el auto (que esta limpio)
# 1ra pasada: G1(90), G2(60), P1(63), 3 aves mas (150)...   Total: 363
# 2da pasada: G1(90), G2(60), P1(44.1), 3 aves mas (150)... Total: 344.1
#                                                 Total ensuciado: 707.1

bandadaInicial.cambiarFormacion("W")
bandadaInicial.ensuciar(auto1)
print(auto1.suciedad)

# 4.f Llevar el auto al lavadero más barato de BsAs y hacerlo lavar

SmallerLav = LavaderoArtesanal(2)   # Más barato que el SmallLav
BuenosAires.lavaderos.append(SmallerLav)
FasterLav = LavaderoAutomatico()    # Precio fijo de 3000
BuenosAires.lavaderos.append(FasterLav)

print(auto2.suciedad)
(BuenosAires.encontrarLavaderoEconomico(auto2)).lavar(auto2)
print(auto2.suciedad)

# SmallLav 600 / Samller 400 / Faster 1000