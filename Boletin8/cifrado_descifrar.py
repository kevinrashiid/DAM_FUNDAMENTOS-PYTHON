"""ENUNCIADO Haz ahora la función que realiza el descifrado del mensaje."""
def decodificar(texto, mapa):
    # Crear conversión inversa: numero -> letra
    numeros_a_letras = {}
    for letra, num in mapa.items():
        numeros_a_letras[num] = letra
    # Quitar espacios del mensaje
    cadena = texto.replace(" ", "")
    # Si hay una cifra suelta al final, se elimina
    if len(cadena) % 2 == 1:
        cadena = cadena[:-1]
    resultado = []
    # Procesar el mensaje en bloques de 2 cifras
    pos = 0
    while pos < len(cadena):
        """Extrae dos cifras consecutivas del mensaje cifrado y las convierte a entero para poder traducirlas usando el diccionario"""
        bloque = int(cadena[pos:pos+2])

        """Solo se traduce si existe en el diccionario"""
        #MUY IMPORNTANTE ESTE IF QUE PREGUNTA SI EL BLOQUE EN EL DICCIONARIO
        if bloque in numeros_a_letras:
            resultado.append(numeros_a_letras[bloque])
        pos += 2
    return "".join(resultado)#ESTO UNE TODOS LOS ELEMENTOS DE UNA LISTA