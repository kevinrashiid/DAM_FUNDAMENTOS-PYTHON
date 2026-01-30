#Funcion1: calcula el cuadrado de un nnumero y lo devuelve
def calcularCuadrado(numero):
    return numero**2
#Funcion2: suma dos numeros
def sumaDosNumeros(numero1, numero2):
    resultado= numero1+numero2
    return resultado

#Funcion3: suma n numeros
def calcula_suma(numeros=[]):
    resultado=0
    for numero in numeros:
        resultado+=numero
        return resultado

def calcula_sumaN(*numeros):
    resultado=0
    for numero in numeros:
        resultado=resultado+numero
        return resultado


print(calcularCuadrado(500))

numero1=100
numero2=300
print(sumaDosNumeros(numero1,numero2))
print(sumaDosNumeros(10,20))

print(calcula_sumaN(3,4,67,7,222,234))