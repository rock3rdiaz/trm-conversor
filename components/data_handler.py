def data_handler():
    tipo_de_cambio = """
    Necestitas convertir a 
    1 - Tienes Pesos y necestias saber su valor en Dolares ( 1 )
    2 - Tienes Dolares y necesitas saber su valor en Pesos ( 0 )
     
        Elige un criterio : 
    """
    opción = int(input(tipo_de_cambio))
    if opción == 1:
        print('col usd')
        pesos_data = (f'Cantidad en pesos: ')
        pesos_data = float(input(pesos_data))
        return pesos_data
        # valor_dolar
        # conversor  division
    elif opción == 0:
        print('usd col')
        dolar_data = (f'Cantidad en Dolares: ')
        dolar_data = float(input(dolar_data))
        return dolar_data
        # valor_pesos
        # conversor Multiplicacion
    else:
        ('No es una opcion corecta intente nuevamente 1 (COL-U1SD) 2 (USD-COL)')

# if  opción or opción == True:
#
# if opción or opción == False:
#
#
# class Datos:
#     def __init__(self):
#         self.pesos = pesos_data
#         self.dolares = dolar_data
