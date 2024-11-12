class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

        def cambiarColor(self, color):
            if color in ['rojo', 'verde', 'amarillo', 'negro', 'blanco']:
                self.color = color

class Auto:
    def __init__(self, modelo, precio, asientos, marca, Motor, registro, cantidadCreados):
        self.modelo = None
        self.precio = 0
        self.marca = None
        cantidadCreados = 0
        self.registro = 0
        self.motor = Motor
        self.asientos = asientos

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
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = 0
        self.tipo = None
        self.registro = 0

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["gasolina", "electrico"]:
            self.tipo = tipo
