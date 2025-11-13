import random


'''Ejercicio 2: Primitiva sin Números Repetidos
Escribir un programa que genere 6 números aleatorios entre 1 y 49 para la primitiva, pero esta vez sin que se repitan.
Requisitos:

Usar una lista para guardar los números generados
Antes de añadir un número, comprobar que no esté ya en la lista
Si el número ya existe, generar otro hasta conseguir uno nuevo
Al final, mostrar los 6 números ordenados de menor a mayor

Ejemplo de salida:'''

# EJERCICIO 1 LOTERÍA PRIMITIVA
'''
import random
listaNumeros=[]
while len(listaNumeros)<6:
    azar=random.randint(1,49)
    if azar not in listaNumeros: # para que no se repitan
        listaNumeros.append(azar) #AÑADIR AL ARRAY
#LISTA NORMAL
print("NORMAL",listaNumeros)

#LISTA ordenada DE MENOR A MAYOR
listaNumeros.sort()
print("ORDENADA",listaNumeros)

#LISTA invertida MAYOR A MENOR
listaNumeros.reverse() #la invierte
print("INVERTIDA",listaNumeros)
'''

#SACAR NUMERO PRIMO
'''
primo =False
num=0
while not primo:
    num=random.randint(1,10)
    primo=True
    for i in range(2,num):
        if num%i==0:
            primo=False
print(num)'''