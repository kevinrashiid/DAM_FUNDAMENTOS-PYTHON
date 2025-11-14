
bandera=False
listaNumeros=[]
while not bandera:
    numero=str(input("INTRODUCE UN NUMERO-- END PARA SALIR: "))
    if numero=="END":
        bandera=True
    else:
        bandera=False
        c = int(numero)
        if c>0 and c<10:
            listaNumeros.append(c)
        else:
            print("tus numeros tienen que ser entre 0 y 10")
print(listaNumeros)
total=0
media=0
for i in range (len(listaNumeros)):
    total=total+listaNumeros[i]
    media=total/len(listaNumeros)
print("total --> ",total)
print("media --> ",media)


