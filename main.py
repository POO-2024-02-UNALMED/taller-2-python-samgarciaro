class Asiento:
    def _init_(self,color, precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color
class Auto:
    def _init_(self,modelo,precio,marca,registro,Motor,cantidadCreados, asientos):
        self.modelo = modelo
        self.precio = precio
        self.marca = marca
        cantidadCreados = 0
        self.registro = registro
        self.motor = Motor
        self.asientos = asientos

    def cantidadAsientos(self):
        contador = 0
        for asiento in self.asientos:
            if asiento is not None:
                contador += 1
        return contador

    def verificarIntegridad(self):
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if asiento.registro != self.motor.registro or asiento.registro != self.registro:
                    return "Las piezas no son originales"
        return "Auto original"
class Motor:
    def _init_(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["gasolina", "electrico"]:
            self.tipo = tipo