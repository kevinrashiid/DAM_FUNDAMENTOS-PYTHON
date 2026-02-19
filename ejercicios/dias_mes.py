


'''4. Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y
un año (por ejemplo 2022) y diga cuántos días tiene (por ejemplo, 30) y el nombre del
mes. Hazlo usando listas. Recuerda que febrero tiene 29 días cuando el año es divisible
por 4 y 28 el resto de los años'''

mes=0
anio=0
aux=[["enero",31]]

'''---------------------------------------'''

numeroMes=(input("Introduce el mes"))
numero=(input("Introduce el anio"))

meses=["enero","febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octumbre","Noviembre","Diciembre"]
dias=[31,28,31,30,31,30,31,31,30,31,30,31]

while mes<1 or mes>12:
    '''para quitar los espacio el .strip'''
    mes=int(input("Introduce un mes").strip())
anio=int(input("Introduce un año:").strip())
if anio%4!=0 and mes==2:
    print(29,mes[mes-1])
else:
    print(dias[mes-1],meses[mes-1])