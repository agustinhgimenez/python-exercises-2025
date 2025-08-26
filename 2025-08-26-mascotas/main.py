from mascota import Mascota
from perro import Perro
from adoptante import Adoptante
from refugio import Refugio



def main():

    refg_1=Refugio()
    


    perr_1 = Perro("eloy", "26-8-2026")
    refg_1.agregar_mascota(perr_1)
    print(refg_1)  # esto imprimirá como lo defina __str__ de Refugio


if __name__ == "__main__":
    main()
