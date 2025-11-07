''' TODO --- EJERCICIOS PARA EL EXAMEN'''
import random

from sympy import false

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

'''7. Escribir un programa que pida un número al usuario que simule ser el precio de un
artículo y escriba el resultado de aplicarle el IVA del 21%'''
'''teclado=int(input("Precio articulo "))
ivaArticulo=(teclado/100)*21
print(teclado+ivaArticulo)'''


'''12. Escribir un programa que genere seis números aleatorios entre el 1 y el 49 (simulando
una primitiva). Por el momento no te preocupes de que algunos números puedan salir
repetidos. Ya resolveremos eso más adelante.'''
'''for i in range(6):
    num=random.randint(1,49) ##6 numeros aletorios entre el 1 y 49
    print(num)'''

'''16. Escribir un programa que genere un número aleatorio entre el 10.000.000 y el
50.000.000 que sea primo'''
###casteos a enteros

'''azar=random.randint(10000000,50000000) ##numero aletorio'''
bandera=True
while bandera:
    azar = random.randint(int(1e7), int(5e7))  ##numero aletorio con notacion cientifica
    for i in range(2,azar/2):
        if azar%i!=0:
            bandera=False
print(azar)








