
class Asiento:
    color = " "
    precio = 0
    registro = 0

    def cambiarColor(self, color):
        if color == "rojo" or color == "verde" or color == "amarillo" or color == "blanco" or color == "negro":
            self.color = color


class Auto:
    modelo = " "
    precio = 0
    Asiento.asientos = []
    marca = " "
    motor = " "
    registro = " "
    cantidadCreados = 0

    def verificarIntegridad(self, registro):
        if Asiento.asiento[0] == registro and Motor.registro:
            return "Auto original"
        else:
            return "Las piezas no son originales"

    def cantidadAsientos():
        numeroAsientos = 0
        if Asiento.asientos != []:
            for asiento in Asiento.asientos:
                if asiento != []:
                    numeroAsientos += 1
        return numeroAsientos

class Motor:
    tipo = ""
    numeroCilindros = 0
    registro = 0

    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        if tipo == "gasolina":
            self.tipo = tipo
        if tipo == "electrico":
            self.tipo = tipo
