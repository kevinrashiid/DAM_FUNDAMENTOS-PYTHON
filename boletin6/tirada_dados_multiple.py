import random  # Importamos la librería para generar números aleatorios

def tiradadosmultiple(numero_dados):  # Función que recibe cuántos dados queremos lanzar
    contador = 0  # Variable para contar cuántas tiradas hacemos
    while True:  # Bucle infinito hasta que todos los dados sean iguales
        contador += 1  # Sumamos 1 porque vamos a hacer una tirada
        tirada = []  # Lista vacía donde guardaremos los valores de los dados
        # Generamos los valores aleatorios de cada dado
        for i in range(numero_dados):
            dado = random.randint(1, 6)  # Número aleatorio entre 1 y 6
            tirada.append(dado)  # Guardamos el valor en la lista
        # Mostramos la tirada en pantalla
        print(" - ".join(map(str, tirada)))
        # Comprobamos si todos los dados son iguales
        if all(dado == tirada[0] for dado in tirada):
            break  # Si todos son iguales, salimos del bucle
    # Mostramos cuántas tiradas fueron necesarias
    print("He tenido que lanzar los dados", contador, "veces para que todos sean iguales")
tiradadosmultiple(3)