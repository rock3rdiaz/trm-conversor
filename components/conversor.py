class Conversor:
    def __init__(self, pesos, dolares, trm):
        self.pesos = pesos
        self.dolares = dolares
        self.trm = trm

    def convert_to_dollars(self):
        return self.pesos / self.trm

    def convert_to_pesos(self):
        return self.dolares * self.trm

"""
class Conversor:
    def __init__(self, exchange_rate):
        self.exchange_rate = exchange_rate

    def convert(self, moneda_origen, cantidad):
        if moneda_origen == 'pesos':
            return cantidad / self.exchange_rate
        elif moneda_origen == 'dolares':
            return cantidad * self.exchange_rate
        else:
            return None

"""