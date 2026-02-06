from itertools import count

def fraccion(fraccion):
    if fraccion.count("/")!=1: #SI EL CONTEO DE "/" ES DIFERENTE A 1 DEVUELVE 0
        return 0.0
    else:
        numerador,denominador=fraccion.split("/")#PONE EL / COMO SEPARADOR
        if not numerador.isnumeric() or not denominador.isnumeric(): # SI EL PRIMER NUMERO Y EL SEGUNDO NO ES NUMERICO DEVUELVE 0
            return 0.0
        return int(numerador)/int(denominador) #DEVUELVE EL RESULTADO DE LA OPERACION
    """UTILIZANDO LA FUNCION"""
print(fraccion("25/10"))
print(fraccion("a/10"))
print(fraccion("10//a"))
print(fraccion("//10"))
print(fraccion("10"))

