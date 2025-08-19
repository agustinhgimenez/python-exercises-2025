class Computadora:
    # (d) Atributo de CLASE para contar cuántas se crean
    contador = 0

    # (a) Constructor 
    def __init__(self, marca, modelo, cpu, ram_gb, storage_gb, gpu, os):
        # Atributos 
        self.marca = marca           
        self.modelo = modelo         
        self.cpu = cpu               
        self.ram_gb = ram_gb          
        self.storage_gb = storage_gb  
        self.gpu = gpu                
        self.os = os                  

        # (e.b)  histórico de mantenimientos
        self.mantenimientos = []

        # (d)  incrementamos el contador de CLASE
        Computadora.contador += 1

    # (b) __str__: representación legible del objeto
    def __str__(self):
        return (f"{self.marca} {self.modelo} | CPU: {self.cpu} | "
                f"RAM: {self.ram_gb}GB | Disco: {self.storage_gb}GB | "
                f"GPU: {self.gpu} | SO: {self.os}")

    # (d) acceso  al contador 
    @classmethod
    def cantidad_creadas(cls):
        return cls.contador

    # (e.a) Actualiza el sistema operativo
    def updateOS(self, nuevo_os):
        self.os = nuevo_os

    # (e.b) Mantenimiento programado 
    def PM(self, nota="Mantenimiento programado"):
        self.mantenimientos.append(nota)

    # (e.c) Instalar más RAM
    def addRAM(self, extra_gb):
        self.ram_gb += extra_gb

    # (e.d) Consultar capacidad de un componente
    def getCapacity(self, componente):
        comp = componente.lower()
        if comp in ("ram", "ram_gb"):
            return self.ram_gb
        if comp in ("storage", "disco", "ssd", "storage_gb"):
            return self.storage_gb
        if comp == "cpu":
            return self.cpu      # para CPU/GPU devuelvo el modelo
        if comp == "gpu":
            return self.gpu
        return "Componente desconocido"
