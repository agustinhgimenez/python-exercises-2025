from libro import Libro, EstadoLibro
from prestamo import Prestamo


class Biblioteca:
    def __init__(self):
        self.libros = set()
        self.socios = set()
        self.prestamos = [] 

    def total_existencias(self):
        return len(self.libros)

    def agregar_libro(self, libro: Libro):
        self.libros.add(libro)

    def eliminar_libro(self, libro: Libro):
        self.libros.remove(libro)

    def prestar_libro(self, socio, libro):
        if libro not in self.libros:
            raise ValueError("El libro no está disponible en la biblioteca")
        if libro.estado == EstadoLibro.ROTO:
            raise ValueError("El libro está roto y no puede prestarse")

        prestamo = Prestamo(socio, libro)
        self.prestamos.append(prestamo)
        socio.retirar(libro)
        self.libros.remove(libro)  # ya no disponible en stock
        return prestamo

    def total_prestamos(self):
        return len(self.prestamos)

    def agregar_socio(self, socio):
        self.socios.add(socio)

    def eliminar_socio(self, socio):
        self.socios.remove(socio)

    def total_socios(self):
        return len(self.socios)
