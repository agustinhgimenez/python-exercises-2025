# Ejercicio: Biblioteca 📚

Modelado de una **biblioteca** en Python utilizando Programación Orientada a Objetos (POO).  
Este ejercicio implementa las clases principales de un sistema de gestión de biblioteca: `Libro`, `Socio` y `Biblioteca`.

---

## 📂 Archivos

- `libro.py` → Clase `Libro` y enumeración de `EstadoLibro`.  
  - Valida duplicados por combinación de *(título, edición, ISBN)*.  
  - Método `__str__` para representación legible.  

- `socio.py` → Clase `Socio`.  
  - Identificado por *nombre* y *DNI*.  
  - Posee una lista de `préstamos` (métodos `retirar` y `devolver` a implementar).  

- `biblioteca.py` → Clase `Biblioteca`.  
  - Mantiene colecciones de libros y socios (usando `set` para evitar duplicados).  
  - Métodos principales:  
    - `agregar_libro` / `eliminar_libro`  
    - `agregar_socio` / `eliminar_socio`  
    - `total_existencias`, `total_socios`  
    - `prestar_libro` y `total_prestamos` (pendientes de implementación).  

- `main.py` → Script de prueba con ejemplos de:  
  - Alta y baja de libros.  
  - Manejo de excepciones al eliminar un libro inexistente.  
  - Alta y baja de socios.  

---


## DER

```mermaid
erDiagram
  BIBLIOTECA ||--o{ SOCIO : "tiene"
  BIBLIOTECA ||--o{ LIBRO : "posee"
  SOCIO ||--o{ PRESTAMO : "realiza"
  LIBRO ||--o{ PRESTAMO : "participa"

  BIBLIOTECA {
    int id_biblioteca PK
    string nombre
    string direccion
  }

  SOCIO {
    string dni PK
    string nombre
    int id_biblioteca FK
  }

  LIBRO {
    int id_ejemplar PK
    string titulo
    int edicion
    string isbn
    string estado
    int id_biblioteca FK
  }

  PRESTAMO {
    int id_prestamo PK
    date fecha_desde
    date fecha_hasta "NULL = activo"
    string estado
    string dni_socio FK
    int id_ejemplar FK
    int id_biblioteca FK
  }


```markdown


## 🚀 Cómo ejecutar

```bash
python3 main.py



