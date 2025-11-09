''' TODO --- EJERCICIOS PARA EL EXAMEN'''
import random
from email.contentmanager import raw_data_manager
from idlelib.macosx import addOpenEventSupport
from typing import final

from unicodedata import numeric

'''1. Escribir un programa donde se muestren los 10 primeros números enteros'''
'''for i in range(1,11):
    print(i)'''

'''2. Escribir un programa donde se muestren los 50 primeros números pare'''
'''
for i in range(1,100):
    if i%2==0&i<50:
        print(i)'''

'''3. Escribir un programa donde se muestren los 5 primeros números múltiplos de uno dado
por el usuario'''
'''teclado=int(input("introduce un numero"))
for i in range(1,6):
    resultado=teclado*i
    print(resultado)'''


'''4. Escribir un programa donde se muestren todos los números divisibles por 7 menores a
10000'''
'''limite=1000
for i in range(1000):
    if(i%7==0&i<1000):
        print(i)'''

'''5. Escribir un programa que pida un número al usuario y diga si es par o impar'''
'''numero=int(input("Par o Impar "))
if numero%2==0:
    print("es par")
else:
    print("es impar")'''
'''6. Escribir un programa que pida un número al usuario y diga si es divisible por 3 o no.'''
'''numero=int(input("TU NUMERO SERA DIVISIBLE POR 3--> "))
if numero%3==0:
    print("es divisivel por 3")
else:
    print("no es divisivel por 3")'''

'''7. Escribir un programa que pida un número al usuario que simule ser el precio de un
artículo y escriba el resultado de aplicarle el IVA del 21%'''
'''teclado=int(input("Precio articulo "))
ivaArticulo=(teclado/100)*21
print(teclado+ivaArticulo)'''

'''8. Escribir un programa que genere un número aleatorio entre el 0 y el 50 y lo muestre'''
'''azar=random.randint(0,50)
print(azar)'''


'''9. Escribir un programa que genere dos números aleatorios simultáneamente entre el 1 y el
6 (simulando una tirada de dos dados)'''
'''dado=random.randint(1,6)
dado2=random.randint(1,6)
print(dado,dado2)'''


'''10. Escribir un programa que nos pida dos números y genere un número aleatorio
comprendido entre ambos. Por el momento no te preocupes de que el primer número
siempre debería de ser menor que el segundo, simplemente no los metas en un orden
incorrecto'''
'''inicio=int(input("DAME EL INICIO"))
final=int(input("DAME EL FIN"))
print("te dare un numero entre ",inicio, " y ",final)
azar=random.randint(inicio,final)
print("El numero azar es ",azar)'''

'''11. Modificar el programa del punto anterior para que si el primer número que metemos es
mayor que el segundo funcione correctamente. Es decir, si metemos en primer lugar el
50 y en segundo el 10 nos debería de generar un número aleatorio entre el 10 y el 50 (y
no entre el 50 y el 10 que no tiene mucha lógica...)'''
'''inicio=int(input("DAME EL INICIO"))
final=int(input("DAME EL FIN"))
print("te dare un numero entre ",inicio, " y ",final)
if inicio >= final:
    print("EL PRIMERO TIENE QUE SER MAS PEQUEÑO QUE EL SEGUNDO")
else:
    azar=random.randint(inicio,final)
    print("El numero azar es ",azar)'''

'''12.-Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando
una primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante'''
'''for i in range(1,7):
    primitiva=random.randint(1,49)
    print(primitiva)'''
'''for i in range(6): ES LO MISMO'''

'''13.-Escribir un programa que nos permita generar una quiniela. Para ello nos debe generar
quince números aleatorios entre el 1 y el 3. Recuerda que los resultados válidos son 1 X
o 2, así que si te sale un 3 lo que tienes que imprimir en pantalla es una X'''
'''for i in range(15):
    quiniela=random.randint(1,3)
    if quiniela==3:
        print("x")
    else:
        print(quiniela)'''

'''14. Escribe un programa que genere números aleatorios entre el 1 y el 1000 sin parar y que
sólo se detenga cuando salga el 666'''
'''azar=0
while azar!=666:
    azar=random.randint(1,1000)
    print(azar)'''


'''15. Escribir un programa que pida un número al usuario y calcule si es primo o no lo es'''


'''16. Escribir un programa que genere un número aleatorio entre el 10.000.000 y el
50.000.000 que sea primo'''
###casteos a enteros

'''azar=random.randint(10000000,50000000) ##numero aletorio''''''
bandera=True
while bandera:
    azar = random.randint(int(1e7), int(5e7))  ##numero aletorio con notacion cientifica
    for i in range(2,int(azar/2)):
        if azar%i!=0:
            bandera=False
print(azar)'''







