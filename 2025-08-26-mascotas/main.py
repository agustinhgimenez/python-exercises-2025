from mascota import Mascota
from perro import Perro
from ave import Ave
from gato import Gato
from adoptante import Adoptante
from refugio import Refugio



def main():

    refg_1=Refugio()
    
    adopt1= Adopante("")

    masc1 = Perro("eloy", "26-8-2026")
    masc2 = Gato("Lula", "24-8-2026")
    masc3 = Ave("Pepito", "13-8-2026")
    refg_1.agregar_mascota(masc1)
    refg_1.agregar_mascota(masc2)
    refg_1.agregar_mascota(masc3)
    print(refg_1)  


if __name__ == "__main__":
    main()
