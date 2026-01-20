
"""La siguiente tabla muestra la población de los 20 países con mas habitantes del mundo
actualizado al año 2021:"""

"""Haced un programa en pyton que nos permita cargar estos datos (nombre del país y
población, solamente) desde el teclado. Los paises deberían de estar en una lista y los
datos de población en otra diferente pero las posiciones deberían de coincidir. Es decir,
Si Pakistan ocupa la posición 5 en una lista su población debería de ocupar la misma
posición en la otra para que exista una correspondencia.
La entrada de datos finaliza cuando se introduzca un -1 como nombre de un país. En
ese momento nuestro programa debería de listar los países con sus poblaciones
respectiva.
NOTA: No es preciso que metas los 20 datos para probar que tu programa funciona.
Seguramente te bastará con tres o cuatro..."""

paises =[]
poblaciones = []
entrada=0

while entrada != -1:
    entrada=input(str("Introduce la poblacion o pais"))
    if entrada == -1:
        entrada=entrada-1
    elif isinstance(entrada,str):
        paises.append(str(entrada))
    elif isinstance(entrada,int):
        poblaciones.append(int(entrada))

print(paises)
print(poblaciones)