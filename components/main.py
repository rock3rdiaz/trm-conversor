from components.data_handler import data_handler
from components.input_handler import input_handler
from components.output_handler import division, multiplicacion

if __name__ == "__main__":

   valor = data_handler()
   trm_usd = input_handler()

   print(valor)
   print(trm_usd)

multiplicacion(valor, trm_usd)

division(trm_usd, valor)

print(int(trm_usd * valor()))
print(int(division()))

