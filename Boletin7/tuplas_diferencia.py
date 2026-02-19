

'''2. Modifica ahora el programa anterior para que cree una tupla con los elementos que están en una u
otra pero no en las dos. Muéstrala ahora ordenados descendentemente. Con el mismo ejemplo del
caso anterior la salida sería esta:
Los elementos que solo aparecen en una son: (180,49,9,4,2,1'''
tupla1 = (1,4,2,5,49,3,75,3)
tupla2 = (3,3,75, 75, 180, 9, 5)

listaAux=[] ##lista vacia
for i in tupla1:
    if i not in tupla2 and i not in listaAux:
        listaAux.append(i)
for i in tupla2:
    if i not in tupla2 and i not in listaAux:
        listaAux.append(i)

listaAux.sort(reverse=True) ##ordenando al reves

listaAux=tuple(listaAux)##TODO reasignamos la lista y la casteamos a tuple
print(listaAux)
