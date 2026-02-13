
listaColores=["Rojo","Verde","Azul","Naranja"]
print(listaColores)

try:
    indice=int(input("Dime una posicion: "))
    print(listaColores[indice])
except ValueError:
    print("El numero no es valido: ")
except IndexError:
    print("Solo tenemos 4")