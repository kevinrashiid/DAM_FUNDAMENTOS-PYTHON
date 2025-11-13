from ipaddress import summarize_address_range
from statistics import median

from unicodedata import numeric


'''
5.-Escribir un programa que pida números enteros por teclado. La ejecución terminará
cuando el usuario introduzca la palabra EXIT. En ese momento debería de mostrar un
mensaje diciendo el número de números introducidos, la suma de todos y su media
aritmética.
6. Modificar el programa anterior para que, además, nos diga han sido el número
mayor y el menor que has introducido'''
'''
bandera =False
listaEnteros=[]
while not bandera:
    numero=(input("introduce numero EXIT para salir"))
    if numero=="EXIT":
        bandera=True
    else:
        c =int(numero)
        listaEnteros.append(c)
print(listaEnteros)
total=0
if bandera:
    for i in range(len(listaEnteros)):
        total=total+listaEnteros[i]
    print("total: ",total)
    media=total/len(listaEnteros)
    print("media ",media)
    listaEnterosSort = sorted(listaEnteros)
    print("el mas pequeño ",listaEnterosSort[0])
    print("el mas grande ",listaEnterosSort[-1])#EL MAS MAYOR'''

'''Escribir un programa en Python que te escriba todos los números primos que hay entre
el 1 y el 100'''
esPrimo=False
primos=""

for i in range(3,101):
    if i%2== 0:
        print(i, " no es primo")
    else:
        e = str(i)
        print(e," es primo")
