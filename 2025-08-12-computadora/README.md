# Ejercicio: Computadora 💻

Ejemplo introductorio de **Programación Orientada a Objetos (POO)** en Python.  
Se modela una clase `Computadora` con atributos, métodos de instancia y de clase.

---

## 📂 Archivos

- `computadora.py` → Clase `Computadora`.  
  - Atributos: marca, modelo, CPU, RAM, almacenamiento, GPU, sistema operativo.  
  - Métodos:
    - `__str__` → representación legible.  
    - `cantidad_creadas` (classmethod) → cuenta cuántas instancias se crearon.  
    - `updateOS` → actualiza sistema operativo.  
    - `PM` → agrega nota de mantenimiento.  
    - `addRAM` → incrementa memoria RAM.  
    - `getCapacity` → devuelve capacidad o modelo de un componente.  

- `main.py` → Script de prueba.  
  - Crea varias computadoras.  
  - Imprime sus datos.  
  - Muestra cantidad de instancias creadas.  
  - Prueba métodos (`updateOS`, `addRAM`, etc.).

---

## 🚀 Cómo ejecutar

```bash
python main.py
