

"""EJERCICIO 7 BOLETIN 8"""
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
    return {
        "A":"87",
        "B":"89",
        "C":"89",
        "D":"89"
    }

def cifrar(mensaje,codigo_cifrado):
    #..aqui ciframos
    return "23324"

def enviar(mensaje_encriptado):
    #.. aqui preparo el mensaje
    print(mensaje_encriptado)
if __name__=="__main__":
    main()
else:
    print("Soy un modulo cargado")
