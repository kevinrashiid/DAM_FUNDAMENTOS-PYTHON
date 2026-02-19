

'''1. Queremos hacer un programa en python que, dada una lista compuesta por
números enteros, pida al usuario un número por teclado y si ese número existe en la
lista lo borre todas las veces que aparezca e imprima el resultado final.
Por ejemplo, si la lista es esta:
lista = [42, 74, 34, 42, 51]
Y el usuario introduce el número 42, tú programa debería de borrar todas las veces que
aparece el número 42 en la lista y el resultado, impreso en la consola, debería de ser
este:
[74, 34, 51]
La lista debería de estar ya en el código del programa (no hace falta que la construyas
de forma interactiva). Puedes usar la que aparece aquí como ejemplo. No olvides
contemplar que el usuario puede introducir un número que no esté en la lista o incluso
algo que no sea un número. Tenlo en cuenta en tu código para que este no se rompa.
Ejemplo de ejecución:
Lista: [42, 74, 34, 42, 51]
Introduce el número que quieres borrar de la lista aa
Solo trabajo con números enteros
Lista: [42, 74, 34, 42, 51]
Introduce el número que quieres borrar de la lista 42
Lista: [74, 34, 51]'''

lista=[2,3,4,4,5,4,6,7,8]
listaNueva=[]
numero=(input("SI TU NUMERO NO ESTA EN LA LISTA LO AÑADO"))
if numero.isdigit():
    numero=int(numero)
    for indice in lista:
        if numero != indice:###si es diferente lo añade
            listaNueva.append(indice)
    print(listaNueva)
else:
    print("INTRODUCE UN ENTERO")

