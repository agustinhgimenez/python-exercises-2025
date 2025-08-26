class Socio:
    def __init__(self,nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.prestamos = []

    def retirar(self, libro):
        self.prestamos.append(libro)

    def devolver(self, libro):
         if libro in self.prestamos:
            self.prestamos.remove(libro)
