import random
from ctypes import pythonapi
from gettext import textdomain
from html.parser import interesting_normal
from queue import PriorityQueue

#4. Escribir un programa que pida al usuario una cadena de texto y la escriba con el
#alfabeto típico de los hackers sustituyendo las letras a por el número 4, las letras e por
#el número 3, las letras i por el número 1 y las letras o por el número 0. Considera que
#las vocales pueden estar escritas en mayúsculas o minúsculas y tiene que funcionar con
#ambas, pero no hace falta que tengas en cuenta que además podrían ir acentuadas
#PISTA: se hace más fácilmente con un switch
#a -> 4
#e -> 3
#i -> 1
#o -> 0
'''
texto=input("INTRODUCE TEXTO-> ")
minusculas=texto.lower()
for i in minusculas:
    if i == 'a' :
        minusculas=minusculas.replace('a','4')
    elif i=='e':
        minusculas=minusculas.replace('e','3')
    elif i=='i':
        minusculas=minusculas.replace('i','1')
    elif i=='o':
        minusculas=minusculas.replace('o','0')
print(minusculas)'''

#ENUNCIADO DADO POR EL CHATTI
#Pide al usuario un texto y muestra:
#El número total de caracteres y sin espacios.
#Cuántas vocales tiene.
#El texto en mayúsculas y minúsculas.
#Si contiene la palabra "python" (sin importar mayúsculas).
#El texto sin espacios al principio ni al final.
#El texto con las vocales reemplazadas por números (a→4, e→3, i→1, o→0)
'''texto=input("INTRODUCIR TEXTO")
texto2=texto
numCaracteres= len(texto)
print("el texto tiene ",numCaracteres," caracteres")
contador=0
for i in texto:
    if i =='a' or i=='e'or i=='i'or i=='o' or i=='u':
        contador=contador+1

if texto.find("python")!=-1 :
    print("python encontrado")
else:
    print("python no encontrado")

print("numero de vocales ",contador)
print("minusculas ",texto.lower())
print("mayusculas ",texto.upper())


sinEspacios=texto.strip()
print("sin Espacios ",sinEspacios)

#sustituir VOCALES
for i in texto:
    if i == 'a' :
        texto=texto.replace('a','4')
    elif i=='e':
        texto=texto.replace('e','3')
    elif i=='i':
        texto=texto.replace('i','1')
    elif i=='o':
        texto=texto.replace('o','0')

#PARA IMPRIMIR AL REVES
print("sustituciones de vocales ",texto)
alReves=""
for x in range(len(texto)-1,-1,-1):
    alReves=alReves+texto[x]
print(alReves)

#SIN VOCALES
for i in texto2:
    if i == 'a' :
        texto2=texto2.replace('a','')
    elif i=='e':
        texto2=texto2.replace('e','')
    elif i=='i':
        texto2=texto2.replace('i','')
    elif i=='o':
        texto2=texto2.replace('o','')
    elif i=='u':
        texto2=texto2.replace('u','')
print("sin vocales ",texto2)'''

#TODO
'''
3.-Realiza un juego que consiste en acertar un numero que el ordenador elige de forma
aleatoria entre 1 y 50. Para ello se leen por teclado una serie de números, para los que
se indica ”mayor”' o “menor”, según sea mayor o menor respecto al numero secreto. El
proceso termina cuando se acierta o cuando se superan el número máximo de intentos
establecidos en 3. Si lo prefieres, puedes parametrizar la dificultad del juego
estableciendo dos variables para el número máximo (50) o el número de intentos (3)
'''

'''numAzar=random.randint(1,50)
print(numAzar)
adivina=int(input("ADIVINA EL NUMERO --> "))
intentos=0
bandera=False
while not bandera:

    if adivina==numAzar:
        print("ACERTASTE!")
        intentos=intentos+4
    elif adivina<numAzar:
        intentos=intentos+ 1
        print("es mas grande")
        adivina = int(input("VUELVE A INTENTARLO --> "))

    elif adivina>numAzar:
        intentos=intentos+1
        print("es mas pequeño")
        adivina = int(input("VUELVE A INTENTARLO --> "))
    if intentos >= 2:
        bandera = True
        print("INTENTOS TERMINADOS")'''

'''4.-Modifica el programa anterior para que el programa te de todos los intentos que
necesites pero que cuando aciertes te informe de cuantas veces has fallado antes de
lograrlo'''
numAzar=random.randint(1,50)
print(numAzar)
adivina=int(input("ADIVINA EL NUMERO --> "))
intentos=0
bandera=False
while not bandera:
    if adivina==numAzar:
        print("ACERTASTE!")
        bandera=True
    elif adivina<numAzar:
        intentos=intentos+ 1
        print("es mas grande")
        adivina = int(input("VUELVE A INTENTARLO --> "))
    elif adivina>numAzar:
        intentos=intentos+1
        print("es mas pequeño")
        adivina = int(input("VUELVE A INTENTARLO --> "))
print("Haz necesitado ",intentos," intentos")