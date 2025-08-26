#!/usr/bin/python
# -*- coding: utf-8 -*-

from mascota import Mascota



class Gato(Mascota):
    def __init__(self, tiempo_rehabilitacion):
        super().__init__(tiempo_rehabilitacion=180)
