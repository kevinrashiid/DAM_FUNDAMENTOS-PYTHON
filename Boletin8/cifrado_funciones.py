

"""EJERCICIO 7 BOLETIN 8"""
from random import random


def main():
    print("Soy el main")
    codigo=codigoEncriptacion()

    #pedido el dato
    mensaje="mensaje"
    enccriptacion=cifrar(mensaje)
    enviar(enccriptacion)

"""FUNCION"""
def codigoEncriptacion():
    #... aqui construimos el diccionario
    ##generar un numero aletorio del 10 al 99
    ##ver si no esta en mi lista y añadirlo
    letras="ABCDEFGHIJKLMÑNOPQRSTUVWXYZ"
    codigo={}
    for letra in letras:
        numero =random.randint(1,99)
        while numero in codigo.values():
            numero = random.randint(1, 99)
            #codigo.update({letra:numero})##añade el numero en su clave que le toca
        codigo[letra]=numero
    return codigo

def cifrar(mensaje,codigo_cifrado):
    #..aqui ciframos
    resultado=""
    mensaje=mensaje.replace(" ","").upper()
    for letra in mensaje:
        resultado=resultado+str(codigo_cifrado[letra])
    if len(resultado)%3!=0:
        faltantes=3-len(resultado) %3
        resultado=resultado.join(
            [str(random.randint(0,9) for i in range(faltantes))]
        )
    return resultado

def enviar(mensaje_encriptado):
    #.. aqui preparo el mensaje
    print(mensaje_encriptado)


if __name__=="__main__":
    main()
else:
    print("Soy un modulo cargado")
