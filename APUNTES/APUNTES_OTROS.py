"""🔥 1️⃣ Facturas pendientes (Boletín Diccionarios – Ejercicio 3)
Escribe un programa en Python que sirva para gestionar las facturas pendientes de cobro de una empresa.
Las facturas se almacenarán en un diccionario donde:
La clave será el número de factura (entero)
El valor será el coste de la factura (puede tener decimales)
El programa debe preguntar al usuario si quiere:
Añadir una nueva factura (A)
Pagar una factura existente (P)
Terminar (T)
Reglas:
No puede haber dos facturas con el mismo número.
No se puede pagar una factura que no exista.
Cuando se paga, se elimina del diccionario.
Después de cada operación se muestra:
Total recaudado
Total pendiente de cobro"""
def gestionar_facturas():
    diccionario = {}
    recaudado = 0
    while True:
        opcion = input("A añadir, P pagar, T terminar: ").upper()
        if opcion == "A":
            try:
                numero = int(input("Numero factura: "))
                importe = float(input("Importe: "))

                if numero in diccionario:
                    print("Ya existe")
                else:
                    diccionario[numero] = importe
            except ValueError:
                print("Datos incorrectos")
        elif opcion == "P":
            try:
                numero = int(input("Numero factura: "))
                if numero in diccionario:
                    recaudado += diccionario[numero]
                    del diccionario[numero]
                    print("Pagada")
                else:
                    print("No existe")
            except ValueError:
                print("Error")
        elif opcion == "T":
            print("Fin del programa")
            break
        print("Recaudado:", recaudado)
        print("Pendiente:", sum(diccionario.values()))
        print()

"""Plantilla función con try/except"""
def fraccion(texto):
    try:
        partes = texto.split("/")
        num = int(partes[0])
        den = int(partes[1])
        return num / den
    except:
        return 0

"""Plantilla validación fecha AÑO BISIESTO"""
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

"""DICCIONARIOS"""
# Crear un diccionario (clave: nombre, valor: nota)
alumnos = {"Ana": 7.5, "Luis": 5.0, "Marta": 9.1, "Carlos": 6.3}

# Añadir un nuevo alumno
alumnos["KEVIN"] = 3.4

# Modificar la nota de un alumno

# Comprobar si un alumno existe
if "Ana" in alumnos:
    print("Ana está en el diccionario")

# Eliminar un alumno
del alumnos["Carlos"]

print("----- RECORRER SOLO CLAVES -----")
for nombre in alumnos.keys():
    print(nombre)

print("----- RECORRER SOLO VALORES -----")
for nota in alumnos.values():
    print(nota)

print("----- RECORRER CLAVE Y VALOR -----")
for nombre, nota in alumnos.items():
    print(nombre, "tiene un", nota)

# Calcular la nota media
media = sum(alumnos.values()) / len(alumnos)
print("La nota media es:", round(media, 2))

#ORDENAR DICCIONARIO POR VALOR
paisesPoblacion = { "España": 47,"Francia": 65, "Italia": 59}
print(sorted(paisesPoblacion.items(), key=lambda items: items[1], reverse=True))