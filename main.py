class Asiento:
    def __init__(self):
        self.color = None
        self.precio = 0
        self.registro = 0

        def cambiarColor(self, color):
            if color in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
                self.color = color

class Auto:
    def __init__(self):
        self.modelo = None
        self.precio = 0
        self.asientos = []
        self.marca = None
        self.motor = Motor
        self.registro = 0
        cantidadCreados = 0

        def cantidadAsientos(self):
            contador = 0
            for i in self.asientos:
                contador += 1
            return contador
        
        def verificarIntegridad(self):
            if self.motor.registro != self.registro:
                return "Las piezas no son originales"
            
            for asiento in self.asientos:
                if isinstance(asiento, Asiento) and asiento.registro != self.registro:
                    return "Las piezas no son originales"
            
            return "Auto original"

class Motor:
    def __init__(self):
        self.numeroCilindros = 0
        self.tipo = None
        self.registro = 0
