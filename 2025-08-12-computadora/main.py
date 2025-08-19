from computadora import Computadora

def main():
    # “Valores por defecto” que elegimos al crear la PC base
    DEFAULT = ("Genérica", "Base", "Intel i3", 8, 256, "Integrada", "Linux")

    # c) Tres computadoras con valores distintos
    pc1 = Computadora(*DEFAULT)
    pc2 = Computadora("Lenovo", "IdeaPad 3", "Ryzen 5 5500U", 16, 512, "Integrada", "Windows 11")
    pc3 = Computadora("Asus", "ROG", "Intel i7-12700F", 32, 1000, "RTX 4070", "Windows 11")

    # b) Mostrar info esencial (__str__)
    print(pc1)
    print(pc2)
    print(pc3)

    # d) Cantidad creadas (atributo de CLASE)
    print("Cantidad creadas:", Computadora.cantidad_creadas())

    # e) Probar métodos
    pc1.updateOS("Ubuntu 24.04")
    pc1.addRAM(8)                  # ahora pc1 tiene 16 GB
    pc1.PM("Cambio de pasta térmica")

    print("RAM pc1:", pc1.getCapacity("ram"), "GB")
    print("Disco pc2:", pc2.getCapacity("storage"), "GB")
    print("GPU pc3:", pc3.getCapacity("gpu"))

if __name__ == "__main__":
    main()
