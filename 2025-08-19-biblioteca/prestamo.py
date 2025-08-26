from datetime import datetime

class Prestamo:
    def __init__(self, socio, libro):
        self.socio = socio
        self.libro = libro
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = None

    def devolver(self):
        self.fecha_devolucion = datetime.now()
