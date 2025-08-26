from mascota import Mascota
from perro import Perro
from adoptante import Adoptante
from refugio import Refugio



def main():

    refg_1=Refugio()
    

    #perr_1= Perro("eloy","26-8-2026",f"{Perro.get_tiempo_rehabilitacion}",f"{Perro.get_alojamiento}")

    perr_1= Perro("eloy","26-8-2026")

    refg_1=Refugio.agregar_mascota(perr_1)

    print(refg_1)
