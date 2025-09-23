class EstadoLibro:
    BUENO = "BUENO"
    ROTO = "ROTO"

class Libro:
    existentes = {} # Conjunto de tuplas (titulo, edicion, isbn)
    def __init__(self, titulo, edicion, isbn):
        self.titulo = titulo
        self.isbn = isbn
        self.edicion = edicion
        self.estado = EstadoLibro.BUENO
        self._validar(self)

    @classmethod
    def _validar(cls, libro):
        clave = (libro.titulo, libro.edicion)
        if clave in cls.existentes:
            if cls.existentes[clave] != libro.isbn:
                raise ValueError(
                    f"Ya existe un libro con titulo '{libro.titulo}', "
                    f"edición '{libro.edicion}' pero con otro ISBN "
                    f"({cls.existentes[clave]} ≠ {libro.isbn})"
                )
        else:
            # Si no existe, lo registramos
            cls.existentes[clave] = libro.isbn

    def __str__(self):
        return f"Titulo: {self.titulo} Edicion: {self.edicion} Isbn: {self.isbn}"


if __name__ == "__main__":
    libro = Libro("100 años de soledad", "1ra", "ABC123")
    libro_falso = Libro("100 años de soledad", "1ra", "DEF456")
