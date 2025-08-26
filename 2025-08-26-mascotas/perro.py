#!/usr/bin/python
# -*- coding: utf-8 -*-

from mascota import Mascota



class Perro(Mascota):
    def __init__(self, tiempo_rehabilitacion,alojamiento):
        super().__init__(tiempo_rehabilitacion=30)
        super().__init__(alojamiento="Cucha")

    def get_tiempo_rehabilitacion(self,tiempo_rehabilitacion):
        self.tiempo_rehabilitacion=tiempo_rehabilitacion

    def get_alojamiento(self,alojamiento):
        self.alojamiento=alojamiento


def __str__(self):
    return f"Nombre : {self.nombre}, Fecha de Ingreso : {self.fecha_ingreso}, Tiempo Rehabilitacion : {self.tiempo_rehabilitacion}, Alojamiento : {self.alojamiento}"


