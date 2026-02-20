import datetime

def fecha_mas_antigua(fecha1, fecha2):
    for fecha in (fecha1, fecha2): #recoremos las dos fechas
        partes = fecha.split("/") #partimos cada fecha en 3 partes
        if len(partes) != 3: #sí es diferente a 3 partes ERROR
            return "Alguna de las fechas no es válida"
        d, m, a = map(int, partes) #mete cada parte en una variable
        if m < 1 or m > 12: #si mes es menor que 1 ERROR O es mayor a 12 ERROR
            return "Alguna de las fechas no es válida"
    d1, m1, a1 = map(int, fecha1.split("/")) #LO MISMO QUE ANTES PERO ACADA FECHA
    d2, m2, a2 = map(int, fecha2.split("/"))

    ##TODO COMPARANDO FECHAS
    if (a1, m1, d1) < (a2, m2, d2):
        return f"La fecha más antigua es {fecha1}"
    elif (a2, m2, d2) < (a1, m1, d1):
        return f"La fecha más antigua es {fecha2}"
    else:
        return "Las dos fechas son iguales"

print(fecha_mas_antigua("20/10/2020","19/10/2020"))