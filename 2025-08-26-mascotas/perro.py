#!/usr/bin/python
# -*- coding: utf-8 -*-

from mascota import Mascota

class Perro(Mascota):
    def __init__(self, nombre, fecha_ingreso, tiempo_rehabilitacion=30, alojamiento="Cucha"):
        super().__init__(nombre, fecha_ingreso, alojamiento)
        self.tiempo_rehabilitacion = tiempo_rehabilitacion

    # Getters
    def get_tiempo_rehabilitacion(self):
        return self.tiempo_rehabilitacion

    def get_alojamiento(self):
        return self.alojamiento

    # Setters (si querés permitir cambiarlos luego)
    def set_tiempo_rehabilitacion(self, valor):
        self.tiempo_rehabilitacion = valor

    def set_alojamiento(self, valor):
        self.alojamiento = valor

    def __str__(self):
        return (f"Nombre del Perro: {self.nombre}, Fecha de Ingreso: {self.fecha_ingreso}, "
                f"Tiempo Rehabilitación: {self.tiempo_rehabilitacion}, "
                f"Alojamiento: {self.alojamiento}")
