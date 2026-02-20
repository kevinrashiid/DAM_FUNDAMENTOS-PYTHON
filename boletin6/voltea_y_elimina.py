def volteayelimina(cadena, caracter):  # Definimos la función con dos parámetros: el texto y el carácter a eliminar
    contador = cadena.count(caracter)  # Contamos cuántas veces aparece el carácter en la cadena
    nueva_cadena = cadena.replace(caracter, "")  # Eliminamos el carácter (lo reemplazamos por vacío "")

    al_reves = nueva_cadena[::-1]  # Invertimos la cadena usando slicing

    print("La cadena al revés y sin el carácter '{}' es: {}".format(caracter, al_reves))
    # Mostramos la cadena ya invertida y sin el carácter

    print("He eliminado", contador, "caracteres")
    # Mostramos cuántos caracteres se han eliminado

volteayelimina("Hola mundo cruel", "o")