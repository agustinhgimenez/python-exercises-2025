from biblioteca import Biblioteca
from libro import Libro
from socio import Socio

def main():
    bibl = Biblioteca()
    print(f"Existencias: {bibl.total_existencias()}")
    libro_1 = Libro("100 años de soledad", "1ra", "ABC123")
    libro_2 = Libro("Las mil y una noches", "3er", "DEF345")
    bibl.agregar_libro(libro_1)
    bibl.agregar_libro(libro_2)
    print(f"Existencias: {bibl.total_existencias()}")
    bibl.eliminar_libro(libro_1)
    try:
        bibl.eliminar_libro(libro_1)
    except Exception as e:
        print(type(e))
        print("Intento eliminar un libro que no existe")


    print(bibl.libros)

    print(f"Existencias: {bibl.total_existencias()}")

    socio_1 = Socio("Carlos", "32333666")
    socio_2 = Socio("Analia", "27555000")

    print(f"Socios: {bibl.total_socios()}")

    bibl.agregar_socio(socio_1)
    bibl.agregar_socio(socio_1)
    bibl.agregar_socio(socio_2)

    print(f"Socios: {bibl.total_socios()}")

    bibl.eliminar_socio(socio_2)

    print(f"Socios: {bibl.total_socios()}")

    # --- Préstamos ---
    print("\n--- Pruebas de préstamos ---")

    # Volvemos a agregar libro_1 para que haya 2 disponibles
    bibl.agregar_libro(libro_1)
    print(f"Existencias: {bibl.total_existencias()}")

    # Prestar un libro a un socio
    prestamo_1 = bibl.prestar_libro(socio_1, libro_1)
    print(f"Préstamo realizado: {prestamo_1.libro.titulo} -> {prestamo_1.socio.nombre}")
    print(f"Existencias después del préstamo: {bibl.total_existencias()}")
    print(f"Total préstamos: {bibl.total_prestamos()}")
    print(f"Libros en manos de {socio_1.nombre}: {[libro.titulo for libro in socio_1.prestamos]}")

    # Intentar prestar el mismo libro de nuevo (debe fallar)
    try:
        bibl.prestar_libro(socio_2, libro_1)
    except Exception as e:
        print("Error esperado:", e)

    # Intentar prestar un libro roto
    libro_2.estado = "ROTO"
    try:
        bibl.prestar_libro(socio_2, libro_2)
    except Exception as e:
        print("Error esperado:", e)




if __name__ == "__main__":
    main()
