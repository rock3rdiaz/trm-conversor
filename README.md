# trm-conversor
## Descripcion
Construiremos un conversor de divisas solamente teniendo en cuenta: COP y USD.
## Flujo principal
El comportamiento general del aplicacion sera el siguiente:
- El usuario debera seleccionar que tipo de conversion requiere. Solo existiran dos posibles casos:
>- COP a USD
>- USD a COP
- El usuario debera definir el monto a convertir. En este punto se permitira el ingreso de cualquier cantidad. Se debe validar el valor ingresado, esto es, debe ser un numero. En caso de que no se ingrese un monto valido la aplicacion debera regresar el mensaje de error ```El monto ingresado no es valido. Solo se aceptan valores numericos.```
- La aplicacion obtendra el valor del TRM desde la API https://www.freeforexapi.com/api/live\?pairs\=USDCOP . La salida del servicio podra verse en ```trm_output.json```
- Con el valor del TRM y dependiendo del tipo de conversion (primer punto), la aplicacion efectuara la conversion solicitada segun sea el caso.
- La aplicacion regresara el valor calculado aplicando formato de moneda (separacion de millones, miles, centimos, etc)

# Notas
La aplicacion se dividira en 4 grandes funcionalidades:
- Componente de lectura de los datos del usuario: Este componente se encargara de leer los datos del usuario y hacer las validaciones necesarias en esta etapa.
- Componente de obtencion del TRM: Este componente tendra bajo su responsabilidad el obtener el valor del TRM desde la fuente indicada en el flujo.
- Componente de negocio: Este sera el componente que tendra la definicion del calculo a realizar segun corresponda.
- Componente de formateo: Este componente le dara el formato correcto al calculo realizado.

Para matenerlo simple, se suguiere una funcion por cada componente descrito (se puede usar un enfoque OO).

Para el componente que obtendra el valor del TRM nos apoyaremos en la libreria https://requests.readthedocs.io/en/latest/ . Se recomienda usar entornos virtuales.
