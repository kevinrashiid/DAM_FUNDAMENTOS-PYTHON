def descifrar(mensaje_cifrado, diccionario):
    # Creamos el diccionario inverso: número -> letra
    dic_inverso = {v: k for k, v in diccionario.items()}

    # Eliminamos los espacios del mensaje cifrado
    cifras = mensaje_cifrado.replace(" ", "")

    # Si queda una cifra suelta al final, se descarta
    if len(cifras) % 2 != 0:
        cifras = cifras[:-1]

    mensaje_descifrado = ""

    # Leemos las cifras de dos en dos
    for i in range(0, len(cifras), 2):
        numero = int(cifras[i:i+2])
        if numero in dic_inverso:
            mensaje_descifrado += dic_inverso[numero]
        # Si no está en el diccionario, se ignora (número aleatorio)

    return mensaje_descifrado
