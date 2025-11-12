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
'''bandera=False
contador=0
while(bandera==False):
    salida=(input("Escribe algo, FIN para salir:"))
    if salida == "FIN":
        bandera=True
        print("SALIMOS")
    else:
        print("no SALIMOS")
        contador=contador+1
        #SIN ACABAR
if(bandera==True):
    print("SALISTE")
    print("Haz introducido ",contador," entradas antes de salir")'''

#7. Escribir un programa en python que pida un número por teclado y nos imprima la tabla
#de multiplicar de dicho número del 1 al 10. Por ejemplo, si introducimos el 74 el
#resultado será algo así:
#74 x 1 = 74
#74 x 2 = 148
#…
#74 x 10 = 740
'''numero=int(input("dime un numero "))
print("TABLA DE MULTIPLICAR DEL ",numero)
for i in range(1,11):
    resultado=numero*i
    print(numero," x ", i, " = ", resultado)'''

#8. Escribir un programa en python que pida una contraseña por teclado (dos veces) y si no
#coinciden nos las vuelva a pedir hasta que lo hagan
'''contra=input("CONTRASEÑA: ")
repetirContra=input("VUELVE A INSTRODUCIR LA CONTRASEÑA: ")
while(contra!=repetirContra):
    print("La contraseña no coinciden vuelve a introducirla")
    contra = input("CONTRASEÑA: ")
    repetirContra = input("VUELVE A INSTRODUCIR LA CONTRASEÑA: ")
if(contra==repetirContra):
    print("LAS CONTRASEÑAS SON IGUALES ADELANTE ")'''

#9. Escribir un programa en python que nos pida nuestro nombre y apellidos (dos peticiones
#hechas en ese orden) y nos lo escriba formateado de la siguiente forma:
#Morales Vázquez, José María
'''nombre=input("NOMBRE? ")
apellido=input("APELLIDO? ")
print(apellido,", ",nombre)'''

#10. Escribir un programa en python que nos pida elegir entre cuatro destinos turísticos
#(Francia, Italia, Chile o Japón) y dependiendo de nuestra respuesta nos diga cual es la
#capital de nuestro destino (París, Roma, Santiago de Chile o Tokio)
'''pais=input("ELIGE UN DESTINO FRANCIA ITALIA CHILE JAPON-> ")
paisMinusculas=pais.lower()
if paisMinusculas== "francia" :
    print("Haz elegido Francia con capital Paris")
elif paisMinusculas=="italia":
    print("Haz elegido Italia con capital Roma")
elif paisMinusculas=="chile":
    print("Haz elegido Chile con capital Santiago de chile")
elif paisMinusculas=="japon":
    print("Haz elegido Japon con capital Tokio")
else:
    print("destino no disponible")'''





