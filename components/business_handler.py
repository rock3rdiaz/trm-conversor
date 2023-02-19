# faltan datos  del input para modificar

class Conversor:
    def __init__(self, pesos_cambio , dolares_cambio ):
        self.pesos = pesos_cambio
        self.dolares = dolares_cambio

    def __str__(self):
        return self.pesos,* self.dolares




