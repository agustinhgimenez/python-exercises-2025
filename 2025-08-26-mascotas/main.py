# main.py
from datetime import date
from refugio import Refugio
from perro import Perro
from gato import Gato
from ave import Ave
from novato import Novato
from benefactor import Benefactor
from adopcion import Adopcion

# Crear el refugio
r = Refugio()

# Fecha de hoy
hoy = date.today()

# Agregar algunas mascotas al refugio con fechas fijas
r.agregar_mascota(Perro(1, "Firulais", date(2023, 5, 1)))  # perro hace mucho tiempo -> disponible
r.agregar_mascota(Perro(2, "Rocco",    date(2023, 9, 1)))  # perro hace poco -> no disponible
r.agregar_mascota(Gato(3,  "Mishi",    date(2022, 10, 1))) # gato hace mucho -> disponible
r.agregar_mascota(Ave(4,   "Pio",      date(2024, 9, 1)))  # ave siempre disponible

# Mostrar mascotas disponibles
print("Mascotas disponibles para adoptar:")
for m in r.listar_disponibles():
    print("-", m.id, m.apodo, m.__class__.__name__)

# Crear adoptantes
nico = Novato("Nico")
caro = Benefactor("Caro")

# Nico (novato) adopta el primer perro disponible
for m in r.listar_disponibles():
    if m.__class__.__name__ == "Perro":
        r.registrar_adopcion(Adopcion(m, nico, hoy))
        print("Nico adoptó a", m.apodo)
        break

# Caro (benefactor) adopta el primer ave disponible
for m in r.listar_disponibles():
    if m.__class__.__name__ == "Ave":
        r.registrar_adopcion(Adopcion(m, caro, hoy))
        print("Caro adoptó a", m.apodo)
        break

# Mostrar historial de adopciones
print("\nHistorial de adopciones:")
for a in r.historial_adopciones():
    print(a.fecha, "-", a.adoptante.nombre, "->", a.mascota.apodo)
