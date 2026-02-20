#TODO VALIDANDO EL NUMERO
def validar_retirada(retirada,saldoActual):
    retirada=int(retirada)
    if retirada <0:
        raise ValueError("No se puede retirar cantidades negativas") # raise lanza el error
    if retirada%20!=0 and retirada%50!=0:
        raise ValueError("Solo multiplos de 20 o 50")
    if retirada >saldoActual:
        raise ValueError("La retirada es mayor que el saldo")
    return retirada

saldo=1000

try:
    retirada=validar_retirada(input("Ingrese el numero de retirada:"),saldo)
    saldo=saldo-retirada
except ValueError as e:
    print(e)
else: #ESTO ES COMO SI HUBIERA UN IF ARRIBA
    print("Saldo restante: ",saldo)
    print("Efectivo: ",retirada)
finally:   #ESTO NO SACA SI O SI
    print("Gracias por usar nuestro servicio")
