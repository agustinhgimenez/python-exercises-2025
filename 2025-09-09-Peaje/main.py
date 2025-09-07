# main.py
from peaje import Peaje, FormaDePago, Auto, Moto, Camion, AutoElectrico, Gubernamental

# ************************ PRUEBAS ************************

peaje = Peaje("Peaje")

# Formas de pago
sube = FormaDePago(0.7)
telepase = FormaDePago(0.5)
efectivo = FormaDePago(1)

# Vehiculos
auto = Auto("AU 234 TO", formaDePago=sube)
moto = Moto("MO 789 TO", formaDePago=efectivo)
camion = Camion("CA 710 NN", ejes=3, formaDePago=telepase)

# *** PUNTO 1 ***

print("Punto 1)")
print(f"[{auto.patente}] total a cobrar: {peaje.cobrar(auto)}")        # Cobrar a un auto con SUBE       - 70
print(f"[{moto.patente}] total a cobrar: {peaje.cobrar(moto)}")        # Cobrar a una moto en efectivo   - 50
print(f"[{camion.patente}] total a cobrar: {peaje.cobrar(camion)}")    # Cobrar a un camion con telepase - 300

# *** PUNTO 2 ***
# Calcular el valor de recaudacion total de los peajes

print("\nPunto 2)")
print(f"Recaudacion total: {peaje.recaudacionTotal()}")  # Resultado esperado 300+50+70 = 420

# *** PUNTO 3 ***
# Encontrar la patente del mejor cliente, aquel que más gasto en los peajes

print("\nPunto 3)")

peaje.cobrar(auto)
peaje.cobrar(auto)
peaje.cobrar(auto)  # Le sumo +70 * 4 al auto
peaje.cobrar(auto)  # En este punto el auto suma un total de 350

# Para verificar:
print(f"[{auto.patente}] - {peaje.totalVehiculo(auto)}")
print(f"[{moto.patente}] - {peaje.totalVehiculo(moto)}")
print(f"[{camion.patente}] - {peaje.totalVehiculo(camion)}")

print(f"El mejor cliente es - {peaje.mejorCliente()}")

# *** PUNTO 4 ***

autoElec = AutoElectrico("EL 327 IC", formaDePago=efectivo)
autoVip = Gubernamental("GO 777 BR", formaDePago=telepase)

print("\nPunto 4)")

# Como paga en efectivo (100) se le cobra el 100%, se aplica el 20% por ser electrico... total a cobrar 20
print(f"[{autoElec.patente}] total a cobrar: {peaje.cobrar(autoElec)}")

# No paga nada el auto gubernamental
print(f"[{autoVip.patente}] total a cobrar: {peaje.cobrar(autoVip)}")
