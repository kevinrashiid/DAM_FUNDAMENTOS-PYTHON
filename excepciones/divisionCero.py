
"""1. El clásico: División por cero
Escribe un programa que pida al usuario dos números y realice una división. Debes capturar la excepción en caso de que el usuario intente dividir por cero.
    • Error a capturar: ZeroDivisionError
    • Reto extra: Si el usuario ingresa una letra en lugar de un número, captura también ese error (ValueError)."""
try:##Casteando a entero para que solo sea numero si no da error
    dividendo=int(input("Introduce un DIVIDENDO: "))
    divisor=int(input("Introduce un DIVISOR: "))
    try:##capturando la division entre 0 QUE DA ERROR
        resultado = dividendo / divisor
        print("El numero ingresado es:", resultado)
    except ZeroDivisionError:
        print("No puedes dividir entre cero")
except:
    print("El numero ingresado no valido")


