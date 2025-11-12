#1.-Escribir un programa en python que nos pida tres números en cualquier
# orden y nos los ### muestre en pantalla de menor a mayor
'''print("TE ORDENARE LOS TRES NUM QUE ME PASES")
num1=int(input("PRIMER NUMERO "))
num2=int(input("SEGUNDO NUMERO "))
num3=int(input("TERCER NUMERO "))

mayor=max(num1,num2,num3)
menor=min(num1,num2,num3)
medio=(num1+num2+num3)-(mayor+menor)
print(menor)
print(medio)
print(mayor)'''
from statistics import median
from tokenize import String

from ejercicio import contador

#3.-Escribir un programa en python que nos pida las notas de los dos trimestres
# y nos muestre la media aritmética resultante
'''primerTri=float(input("NOTA PRIMER TRIMESTRE"))
segundoTri=float(input("NOTA SEGUNDO TRIMESTRE"))

sumaTrimestre=float(primerTri+segundoTri)
media=sumaTrimestre/2.0
print("la media es ",media)'''

#4.-Escribir un programa en python que nos pida las notas obtenidas en un trimestre y nos
#muestre la media ponderada sabiendo que;
#◦ La primera nota corresponde al trabajo en clase y cuenta como un 10% del total
#◦ La segunda corresponde a los ejercicios prácticos: 20%
#◦ La tercera la nota del examen: 70%
'''notaTrabajos=float(input("NOTA DE TRABAJOS: ")) # 10%
notaEjercicios=float(input("NOTA EJERCICIOS: ")) #20%
notaExamen=float(input("NOTA EXAMEN: ")) #70%

notaTrabajos=notaTrabajos*0.1
notaEjercicios=notaEjercicios*0.2
notaExamen=notaExamen*0.7

medianNotas=notaTrabajos+notaEjercicios+notaExamen

print("La media de las notas ",medianNotas)
'''

#5. Modifica el ejercicio anterior para que cuando la media salga como aprobado pero el
#alumno tenga menos de un 4,5 en cualquiera de los apartados la nota resultante será
#un 4
'''notaTrabajos=float(input("NOTA DE TRABAJOS: ")) # 10%
notaEjercicios=float(input("NOTA EJERCICIOS: ")) #20%
notaExamen=float(input("NOTA EXAMEN: ")) #70%
mediaNotas=0.0

if (notaExamen<4.5 or notaEjercicios<4.5 or notaTrabajos<4.5):
    medianNotas=4.0
    print("NO APROBASTE, la media de las notas ", medianNotas)

else:
    notaTrabajos=notaTrabajos*0.1
    notaEjercicios=notaEjercicios*0.2
    notaExamen=notaExamen*0.7
    medianNotas=notaTrabajos+notaEjercicios+notaExamen
    print("La media de las notas ",medianNotas)'''

#6. Escribir un programa en python que pida una entrada por teclado hasta que escribamos
#la palabra FIN (con mayúsculas). En ese caso terminamos y mostramos por pantalla el
#numero de entradas válidas que hemos hecho (sin contar esta última que sólo sirve para
#finalizar el programa)
bandera=False
contador=0
while(bandera==False):
    salida=String(input("Escribe algo, FIN para salir:"))
    if salida == "FIN":
        bandera=True
    else:
        contador=contador+1
        #SIN ACABAR