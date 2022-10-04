from components.data_handler import data_handler
from components.input_handler import input_handler
from components.output_handler import division, multiplicacion

if __name__ == "__main__":

   valor = data_handler()
   trm_usd = input_handler()

   print(valor)
   print(trm_usd)

operacion1 = multiplicacion(valor, trm_usd)

operacion2 = division(trm_usd, valor)

print(int(operacion2))
print(int(operacion1))

