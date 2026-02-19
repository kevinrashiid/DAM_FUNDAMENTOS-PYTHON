

lista=[]
numero=0
suma=0
contador=0
while numero>=0:
    numero=float(input("INPUT NUMERO"))
    if numero>=0:
        lista.append(numero)
        suma += numero
        contador+=1
    else:
        print("SALI DEL BUCLE")
        numero=-1
    lista.sort()
print("media "+suma/contador)
print(lista)