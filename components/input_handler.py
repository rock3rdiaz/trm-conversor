def get_user_input():
    tipo_de_cambio = """
    ¿Qué tipo de cambio desea realizar?
    1. Pesos a dólares
    2. Dólares a pesos

    Seleccione una opción: """
    conversion = input(tipo_de_cambio)
    if conversion not in ["1", "2"]:
        print("Opción inválida. Por favor, seleccione 1 o 2 e intente nuevamente.")
        return None

    if conversion == "1":
        cantidad = float(input("Ingrese la cantidad de pesos a convertir: "))
        return {"moneda_origen": "pesos", "cantidad": cantidad, "conversion": "1"}
    else:
        cantidad = float(input("Ingrese la cantidad de dólares a convertir: "))
        return {"moneda_origen": "dolares", "cantidad": cantidad, "conversion": "2"}























