'''1. Escribe un programa que dado dos tuplas diferentes nos cree otra con los elementos comunes a
ambas ordenada de forma ascendente y sin repeticiones. Ejemplo:
tupla1 = (1,4,2,5,49,3,75,3)
tupla2 = (3,3,75, 75, 180, 9, 5)
La salida debería de ser así:
Los elementos repetidos en ambas son: (3,5,75)'''

tupla1 = (1,4,2,5,49,3,75,3)
tupla2 = (3,3,75, 75, 180, 9, 5)

listaAux=[] ##lista vacia
for i in tupla1:
    for j in tupla2:
        ##TODO si la i es igual a j Y la i no esta en la listaAux lo añada
        if i==j and i not in listaAux:
            listaAux.append(i)
listaAux.sort() ##ordenando
listaAux=tuple(listaAux)##TODO reasignamos la lista y la casteamos a tuple
print(listaAux)

